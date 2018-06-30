import pandas

def getChange(current, previous):
    negative = 0
    if current < previous:
        negative = True
    try:
        value = (abs(current - previous) / previous) * 100.0
        value = float('%.2f' % value)
        if value >= 0.01 and negative:
            value = value * -1
        return value
    except ZeroDivisionError:
        return 0

data = pandas.read_csv("results/statweights.txt",usecols=['profile','actor','DD','DPS'])

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

# ['profile','actor','DD','DPS']
for value in data.iterrows():
    weight = weights.get(value[1].profile)
    weightedDPS = weight * value[1].DPS
    if value[1].actor in results:
        results[value[1].actor] = results.get(value[1].actor) + weightedDPS
    else:
        results[value[1].actor] = weightedDPS

baseDPS = results.get('Base')

keyList = results.keys()
keyList.sort()
with open('README.md', 'w') as file:
    file.write('| Actor | DPS | Increase |\n|---|:---:|:---:|\n')
    for key, value in sorted(results.iteritems(), key=lambda (k,v): (v,k), reverse=True):
        file.write("|%s|%.0f|%.2f%%|\n" % (key, value, getChange(value, baseDPS)))
