import os
import argparse
import sys
import secrets
import weights as fightWeights
import subprocess

from os import listdir
from subprocess import PIPE, STDOUT

profiles = []
apiKey = secrets.apiKey
version = 'nightly'
weights = '-s'
weightsSingle = fightWeights.weightsSingle
weightsATBT = fightWeights.weightsATBT

parser = argparse.ArgumentParser(description='Parses a list of reports from Raidbots.')
parser.add_argument('dir', help='Directory you wish to sim. Options are 1. talents/ 2. racials/ 3. gear/ 4. enchants/ 5. consumables/ 6. azerite-traits/')
parser.add_argument('--weights', help='For sims ran with weights this flag will change how simParser is ran.', action='store_true')
parser.add_argument('--iterations', help='Pass through specific iterations to run on. Default is "smart"')
parser.add_argument('--composite', help='Run a raidsimming batch of sims. Value can be either HH or MM.', choices=['HC','MM'])
parser.add_argument('--talents', help='indicate talent build for output.', choices=['LotV','DA'])
args = parser.parse_args()

if args.weights:
    weights = ''

if int(args.iterations) > 0:
    iterations = args.iterations
else:
    iterations = "smart"

sys.path.insert(0, args.dir)
import reports

print("Running sims on {0} in {1}".format(version, args.dir))

# determine sim files
if args.composite:
    for value in reports.reportsRS:
        profile = value.replace('results/_', 'profiles/%s_' % args.composite)
        profile = profile.replace('json', 'simc')
        profiles.append(profile)
else:
    for value in reports.reports:
        profile = value.replace('results', 'profiles')
        profile = profile.replace('json', 'simc')
        profiles.append(profile)

# determine existing jsons
existing = listdir(args.dir + 'results/')
count = 0

for value in profiles:
    count = count + 1
    if not args.composite:
        lookup = value[9:-5]
        if args.dir == "talents/" or args.dir == "trinkets/" or args.dir == "stats/":
            lookup = lookup[lookup.index('_')+1:]
        weight = weightsATBT.get(lookup)
        weightST = weightsSingle.get(lookup)
        if weightST:
            weight = weight + weightST
    else:
        weight = 1
    print("Simming {0} out of {1}.".format(count, len(profiles)))
    name = value.replace('simc', 'json')
    name = name.replace('profiles', 'results')
    if name[8:] not in existing and weight > 0:
        reportName = args.dir + name[8:-5]
        name = args.dir + name
        value = args.dir + value
        subprocess.call(['python', 'api.py', apiKey, value, '--simc_version', version, name, reportName, '--iterations', iterations], shell=False)
    elif weight == 0:
        print("{0} has a weight of 0. Skipping file.".format(name[8:]))
    else:
        print("{0} already exists. Skipping file.".format(name[8:]))

results_dir = args.dir + "results/"
subprocess.call(['python', 'simParser.py', '-c', weights, '-r', '-d', results_dir], shell=False)

# analyze.py
if args.composite:
    script = "analyzeRS.py"
else:
    script = "analyze.py"

cmd = "python {0} {1}".format(script, args.dir)

if args.weights:
    cmd += " --weights"
if args.composite:
    cmd += " --composite {0}".format(args.composite)
if args.talents:
    cmd += " --talents {0}".format(args.talents)
subprocess.call(cmd, shell=True)
