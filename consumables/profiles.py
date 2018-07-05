import reports
import os
import shutil
import argparse

# clear out results
for the_file in os.listdir('results/'):
    file_path = os.path.join('results/', the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

# clear out profiles
for the_file in os.listdir('profiles/'):
    file_path = os.path.join('profiles/', the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

parser = argparse.ArgumentParser(description='Generates sim profiles.')
parser.add_argument('--composite', help='Run a raidsimming batch of sims. Value can be either HH or MM.', choices=['HC','MM'])
args = parser.parse_args()

simc = 'consumables.simc'

small_add = 'raid_events+=/adds,count=3,first=45,cooldown=45,duration=10,distance=5'
big_add = 'raid_events+=/adds,count=1,first=30,cooldown=60,duration=20'

patchwerk = 'fight_style="Patchwerk"'
light_movement = 'fight_style="LightMovement"'
heavy_movement = 'fight_style="HeavyMovement"'

# --composite [HC, MM]
if args.composite:
    taloc = '%s_Taloc.simc' % args.composite
    mother_early = '%s_Mother_Early.simc' % args.composite
    mother_late = '%s_Mother_Late.simc' % args.composite
    fetid = '%s_FetidDevourer.simc' % args.composite
    zekvoz = '%s_Zekvoz.simc' % args.composite
    vectis = '%s_Vectis.simc' % args.composite
    zul = '%s_Zul.simc' % args.composite
    mythrax = '%s_Mythrax.simc' % args.composite
    ghuun = '%s_Ghuun.simc' % args.composite

with open(simc, 'r') as f:
    data = f.read()
    f.close()

profiles = []

if args.composite:
    for value in reports.reportsRS:
        profile = value.replace('results/_', 'profiles/%s_' % args.composite)
        profile = profile.replace('json', 'simc')
        profiles.append(profile)
    # create profiles
    for value in profiles:
        settings = '\n'
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

        with open(value, "w+") as f:
            f.writelines(data)
            f.writelines(settings)
            f.close()
else:
    for value in reports.reports:
        profile = value.replace('results', 'profiles')
        profile = profile.replace('json', 'simc')
        profiles.append(profile)
    # create profiles
    for value in profiles:
        settings = '\n'
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

        with open(value, "w+") as f:
            f.writelines(data)
            f.writelines(settings)
            f.close()
