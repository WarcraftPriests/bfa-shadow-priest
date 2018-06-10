import os
import argparse
import sys
import secrets

from os import listdir
from os.path import isfile, join

profiles = []
apiKey = secrets.apiKey
version = 'bfa-dev'

parser = argparse.ArgumentParser(description='Parses a list of reports from Raidbots.')
parser.add_argument('dir', help='Directory you wish to sim. Options are 1. talents/ 2. racials/ 3. gear/ 4. enchants/ 5. consumables/ 6. azerite-traits/')
args = parser.parse_args()

sys.path.insert(0, args.dir)
import reports

print "Running sims on {0} in {1}".format(version, args.dir)

# determine sim files
for value in reports.reports:
    profile = value.replace('results', 'profiles')
    profile = profile.replace('json', 'simc')
    profiles.append(profile)

# determine existing jsons
existing = listdir(args.dir + 'results/')
count = 0

for value in profiles:
    count = count + 1
    print "Simming {0} out of {1}.".format(count, len(profiles))
    name = value.replace('simc', 'json')
    name = name.replace('profiles', 'results')
    if name[8:] not in existing:
        name = args.dir + name
        value = args.dir + value
        cmd = "python3 api.py {0} {1} --simc_version {2} {3}".format(apiKey, value, version, name)
        os.system(cmd)
    else:
        print "{0} already exists. Skipping file.".format(name[8:])

results_dir = args.dir + "results/"
cmd = "python simParser.py -c -s -r -d {0}".format(results_dir)
os.system(cmd)
