import reports
import os
import shutil
import argparse

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

# Set Dungeon Talent Builds manually
# SWV_DV_SC_MB_[DA/LotV]
dungeonsLotV = 'talents=3131312'
dungeonsDA = 'talents=3131311'

parser = argparse.ArgumentParser(description='Generates sim profiles.')
parser.add_argument('dir', help='Directory to generate profiles for.')
parser.add_argument('--dungeons', help='Run a dungeonsimming batch of sims.', action='store_true')
parser.add_argument('--talents', help='indicate talent build for output.', choices=['LotV','DA'])
args = parser.parse_args()

# clear out results
assure_path_exists('%sresults/' % args.dir)
for the_file in os.listdir('%sresults/' % args.dir):
    file_path = os.path.join('%sresults/' % args.dir, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

# clear out profiles
assure_path_exists('%sprofiles/' % args.dir)
for the_file in os.listdir('%sprofiles/' % args.dir):
    file_path = os.path.join('%sprofiles/' % args.dir, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

if args.dir == "apl/":
    simc = '%sapl.simc' % args.dir
elif args.dir == "azerite-trait-ilvls/":
    if args.talents:
        simc = "{0}azerite_{1}.simc".format(args.dir, args.talents)
    else:
        print("Error: must provide --talents [DA, LotV]")
        exit()
elif args.dir in ("consumables/", "enchants/", "racials/", "gear/"):
    if args.dir == "gear/":
        category = "gear_combo_mythic"
    else:
        category = args.dir[:-1]
    if args.talents:
        simc = "{0}{1}_{2}.simc".format(args.dir, category, args.talents)
    else:
        print("Error: must provide --talents [DA, LotV]")
        exit()
elif (args.dir == "trinkets/" or args.dir == "azerite-traits/") and not args.talents:
    print("Error: must provide --talents [DA, LotV]")
    exit()
elif args.dir not in ("stats/", "talents/", "trinkets/", "azerite-gear/", "azerite-traits/"):
    print("Error: provided directory does not match known directory.")
    exit()

small_add = 'raid_events+=/adds,count=3,first=45,cooldown=45,duration=10,distance=5'
big_add = 'raid_events+=/adds,count=1,first=30,cooldown=60,duration=20'

patchwerk = 'fight_style="Patchwerk"'
light_movement = 'fight_style="LightMovement"'
heavy_movement = 'fight_style="HeavyMovement"'
dungeons = 'fight_style="DungeonSlice"'

profiles = []
if args.dir == "stats/":
    report = reports.reportsStats
    DSreport = reports.reportsDungeonsStats
elif args.dir == "talents/":
    report = reports.reportsTalents
    DSreport = reports.reportsDungeonsTalents
elif args.dir == "trinkets/":
    report = reports.reportsTrinkets
    DSreport = reports.reportsDungeonsTrinkets
elif args.dir == "azerite-gear/":
    report = reports.reportsAzerite
    DSreport = reports.reportsDungeonsAzerite
elif args.dir == "azerite-traits/":
    report = reports.reportsAzeriteTraits
    DSreport = reports.reportsDungeonsAzeriteTraits
else:
    DSreport = reports.reportsDungeons
    report = reports.reports

if args.dungeons:
    for value in DSreport:
        profile = value.replace('results', 'profiles')
        profile = profile.replace('json', 'simc')
        profiles.append(profile)
else:
    for value in report:
        profile = value.replace('results', 'profiles')
        profile = profile.replace('json', 'simc')
        profiles.append(profile)

for value in profiles:
    if args.dir == "stats/":
        if "da1" in value:
            simc = '%stalents_DA_1.simc' % args.dir
        if "da2" in value:
            simc = '%stalents_DA_2.simc' % args.dir
        if "lotv1" in value:
            simc = '%stalents_LotV_1.simc' % args.dir
        if "lotv2" in value:
            simc = '%stalents_LotV_2.simc' % args.dir
        if "stm1" in value:
            simc = '%stalents_STM_1.simc' % args.dir
        if "stm2" in value:
            simc = '%stalents_STM_2.simc' % args.dir
    elif args.dir == "talents/":
        if "da" in value:
            simc = '%stalents_DA.simc' % args.dir
        if "lotv" in value:
            simc = '%stalents_LotV.simc' % args.dir
        if "stm" in value:
            simc = '%stalents_STM.simc' % args.dir
    elif args.dir == "trinkets/":
        if "dungeons" in value:
            simc = "{0}trinkets_dungeons_{1}.simc".format(args.dir, args.talents)
        if "other" in value:
            simc = "{0}trinkets_other_{1}.simc".format(args.dir, args.talents)
        if "raid" in value:
            simc = "{0}trinkets_raid_{1}.simc".format(args.dir, args.talents)
    elif args.dir == "azerite-gear/":
        if "chest" in value:
            simc = "{0}chest_{1}.simc".format(args.dir, args.talents)
        if "head" in value:
            simc = "{0}head_{1}.simc".format(args.dir, args.talents)
        if "shoulders" in value:
            simc = "{0}shoulders_{1}.simc".format(args.dir, args.talents)
    elif args.dir == "azerite-traits/":
        if "other" in value:
            simc = "{0}other_{1}.simc".format(args.dir, args.talents)
        if "raid" in value:
            simc = "{0}raid_{1}.simc".format(args.dir, args.talents)
        if "shadow" in value:
            simc = "{0}shadow_{1}.simc".format(args.dir, args.talents)
    with open(simc, 'r') as f:
        data = f.read()
        f.close()
    settings = '\n'
    if args.dungeons:
        settings = settings + dungeons + "\n"
        if args.talents and not args.dir == "talents/":
            if args.talents == "LotV":
                settings = settings + dungeonsLotV
            else:
                settings = settings + dungeonsDA
    else:
        if "pw" in value:
            settings = settings + patchwerk + "\n"
        if "lm" in value:
            settings = settings + light_movement + "\n"
        if "hm" in value:
            settings = settings + heavy_movement + "\n"
        if "ba" in value:
            settings = settings + big_add + "\n"
        if "sa" in value:
            settings = settings + small_add + "\n"
        if "1" in value:
            settings = settings + 'desired_targets="1"' + "\n"
        else:
            settings = settings + 'desired_targets="2"' + "\n"
    with open(args.dir + value, "w+") as f:
        f.writelines(data)
        f.writelines(settings)
        f.close()
