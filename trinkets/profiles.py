import reports
import os
import shutil

folder = 'results/'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

small_add = 'raid_events+=/adds,count=3,first=45,cooldown=45,duration=10,distance=5'
big_add = 'raid_events+=/adds,count=1,first=30,cooldown=60,duration=20'

patchwerk = 'fight_style="Patchwerk"'
light_movement = 'fight_style="LightMovement"'
heavy_movement = 'fight_style="HeavyMovement"'

profiles = []

for value in reports.reports:
    profile = value.replace('results', 'profiles')
    profile = profile.replace('json', 'simc')
    profiles.append(profile)

for value in profiles:
    if "dungeons" in value:
        file = 'trinkets_dungeons.simc'
    if "other" in value:
        file = 'trinkets_other.simc'
    if "raid" in value:
        file = 'trinkets_raid.simc'
    with open(file, 'r') as f:
        data = f.read()
        f.close()
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
