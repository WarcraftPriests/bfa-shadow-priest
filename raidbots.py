import requests
import os

reports = {
    'results/pw_ba_1.json': 'tbd',
    'results/pw_na_1.json': 'tbd',
    'results/pw_sa_1.json': 'tbd',
    'results/lm_ba_1.json': 'tbd',
    'results/lm_na_1.json': 'tbd',
    'results/lm_sa_1.json': 'tbd',
    'results/hm_ba_1.json': 'tbd',
    'results/hm_na_1.json': 'tbd',
    'results/hm_sa_1.json': 'tbd',
    'results/pw_ba_2.json': 'tbd',
    'results/pw_na_2.json': 'tbd',
    'results/pw_sa_2.json': 'tbd',
    'results/lm_ba_2.json': 'tbd',
    'results/lm_na_2.json': 'tbd',
    'results/lm_sa_2.json': 'tbd',
    'results/hm_ba_2.json': 'tbd',
    'results/hm_na_2.json': 'tbd',
    'results/hm_sa_2.json': 'tbd',
}

for key, value in reports.iteritems():
    url = "https://www.raidbots.com/reports/" + value + "/data.json"
    r = requests.get(url)
    with open(key ,'wb') as f:
        f.write(r.content)

os.system('python simParser.py -c -s -r -d results')
