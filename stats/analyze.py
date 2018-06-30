import pandas

data = pandas.read_csv("stats/results/statweights.txt",usecols=['profile','actor','DD','DPS','int','haste','crit','mastery','vers'])

weights = {
    'pw_ba_1': 0.04090909091,
    'pw_sa_1': 0.05000000000,
    'pw_na_1': 0.17272727270,
    'lm_ba_1': 0.02727272727,
    'lm_sa_1': 0.08181818182,
    'lm_na_1': 0.17727272730,
    'hm_ba_1': 0.01818181818,
    'hm_sa_1': 0.17727272730,
    'hm_na_1': 0.02272727273,
    'pw_ba_2': 0.02272727273,
    'pw_sa_2': 0.00000000000,
    'pw_na_2': 0.07272727273,
    'lm_ba_2': 0.06363636364,
    'lm_sa_2': 0.00000000000,
    'lm_na_2': 0.05909090909,
    'hm_ba_2': 0.01363636364,
    'hm_sa_2': 0.00000000000,
    'hm_na_2': 0.00000000000,
}

results = {}

# ['profile','actor','DD','DPS','int','haste','crit','mastery','vers']
for value in data.iterrows():
    profile = value[1].profile
    weight = weights.get(profile[profile.index('_')+1:])
    weightedDPS = weight * value[1].DPS
    if value[1].actor in results:
        existing = results.get(value[1].actor)
        results[value[1].actor] = [
                                    existing[0] + weightedDPS,
                                    existing[1] + weight,
                                    existing[2] + value[1].haste,
                                    existing[3] + value[1].crit,
                                    existing[4] + value[1].mastery,
                                    existing[5] + value[1].vers,
                                  ]
    else:
        results[value[1].actor] = [weightedDPS,weight,value[1].haste,value[1].crit,value[1].mastery,value[1].vers]

with open('stats/README.md', 'w') as file:
    file.write('| Actor | DPS | Int | Haste | Crit | Mastery | Vers |\n|---|:---:|:---:|:---:|:---:|:---:|:---:|\n')
    for key, value in results.items():
        file.write("|%s|%.0f|%.2f|%.2f|%.2f|%.2f|%.2f|\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5]))
