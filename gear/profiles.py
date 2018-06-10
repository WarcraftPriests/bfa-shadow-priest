file = 'Priest_Shadow_T22N.simc'
#file = 'Priest_Shadow_T22H.simc'
#file = 'Priest_Shadow_T22M.simc'

small_add = 'raid_events+=/adds,count=3,first=45,cooldown=45,duration=10,distance=5'
big_add = 'raid_events+=/adds,count=1,first=30,cooldown=60,duration=20'

patchwerk = 'fight_style="Patchwerk"'
light_movement = 'fight_style="Light Movement"'
heavy_movement = 'fight_style="Heavy Movement"'

reports = [
    'profiles/pw_ba_1.simc',
    'profiles/pw_na_1.simc',
    'profiles/pw_sa_1.simc',
    'profiles/lm_ba_1.simc',
    'profiles/lm_na_1.simc',
    'profiles/lm_sa_1.simc',
    'profiles/hm_ba_1.simc',
    'profiles/hm_na_1.simc',
    'profiles/hm_sa_1.simc',
    'profiles/pw_ba_2.simc',
    'profiles/pw_na_2.simc',
    'profiles/pw_sa_2.simc',
    'profiles/lm_ba_2.simc',
    'profiles/lm_na_2.simc',
    'profiles/lm_sa_2.simc',
    'profiles/hm_ba_2.simc',
    'profiles/hm_na_2.simc',
    'profiles/hm_sa_2.simc',
]

with open(file, 'r') as f:
    data = f.read()
    f.close()

for value in reports:
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
