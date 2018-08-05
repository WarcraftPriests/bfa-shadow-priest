import reports
import os
import shutil
import argparse

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

parser = argparse.ArgumentParser(description='Generates sim profiles.')
parser.add_argument('dir', help='Directory to generate profiles for.')
parser.add_argument('--composite', help='Run a raidsimming batch of sims. Value can be either HH or MM.', choices=['HC','MM'])
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
elif args.dir == "azerite-traits/":
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
elif args.dir == "trinkets/" and not args.talents:
    print("Error: must provide --talents [DA, LotV]")
    exit()
elif args.dir not in ("stats/", "talents/", "trinkets/", "azerite-gear/"):
    print("Error: provided directory does not match known directory.")
    exit()

small_add = 'raid_events+=/adds,count=3,first=45,cooldown=45,duration=10,distance=5'
big_add = 'raid_events+=/adds,count=1,first=30,cooldown=60,duration=20'

patchwerk = 'fight_style="Patchwerk"'
light_movement = 'fight_style="LightMovement"'
heavy_movement = 'fight_style="HeavyMovement"'

# --composite [HC, MM]
if args.composite:
    with open("raidsimming/{0}/{1}_Taloc.simc".format(args.composite,args.composite), 'r') as sim:
        taloc = sim.read()
        sim.close()
    with open("raidsimming/{0}/{1}_Mother_Early.simc".format(args.composite,args.composite), 'r') as sim:
        mother_early = sim.read()
        sim.close()
    with open("raidsimming/{0}/{1}_Mother_Late.simc".format(args.composite,args.composite), 'r') as sim:
        mother_late = sim.read()
        sim.close()
    with open("raidsimming/{0}/{1}_FetidDevourer.simc".format(args.composite,args.composite), 'r') as sim:
        fetid = sim.read()
        sim.close()
    with open("raidsimming/{0}/{1}_Zekvoz.simc".format(args.composite,args.composite), 'r') as sim:
        zekvoz = sim.read()
        sim.close()
    with open("raidsimming/{0}/{1}_Vectis.simc".format(args.composite,args.composite), 'r') as sim:
        vectis = sim.read()
        sim.close()
    with open("raidsimming/{0}/{1}_Zul.simc".format(args.composite,args.composite), 'r') as sim:
        zul = sim.read()
        sim.close()
    with open("raidsimming/{0}/{1}_Mythrax.simc".format(args.composite,args.composite), 'r') as sim:
        mythrax = sim.read()
        sim.close()
    with open("raidsimming/{0}/{1}_Ghuun.simc".format(args.composite,args.composite), 'r') as sim:
        ghuun = sim.read()
        sim.close()

profiles = []
if args.dir == "stats/":
    RSreport = reports.reportsRSStats
    report = reports.reportsStats
elif args.dir == "talents/":
    RSreport = reports.reportsRSTalents
    report = reports.reportsTalents
elif args.dir == "trinkets/":
    RSreport = reports.reportsRSTrinkets
    report = reports.reportsTrinkets
elif args.dir == "azerite-gear/":
    RSreport = reports.reportsRSAzerite
    report = reports.reportsAzerite
else:
    RSreport = reports.reportsRS
    report = reports.reports

if args.composite:
    for value in RSreport:
        profile = value.replace('results/_', 'profiles/%s_' % args.composite)
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
    with open(simc, 'r') as f:
        data = f.read()
        f.close()
    settings = '\n'
    if args.composite:
        if "Taloc" in value:
            settings = settings + taloc + "\n"
        if "Mother_Early" in value:
            settings = settings + mother_early + "\n"
        if "Mother_Late" in value:
            settings = settings + mother_late + "\n"
        if "Fetid" in value:
            settings = settings + fetid + "\n"
        if "Zekvoz" in value:
            settings = settings + zekvoz + "\n"
        if "Vectis" in value:
            settings = settings + vectis + "\n"
        if "Zul" in value:
            settings = settings + zul + "\n"
        if "Mythrax" in value:
            settings = settings + mythrax + "\n"
        if "Ghuun" in value:
            settings = settings + ghuun + "\n"
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
