import pandas
import argparse
import operator
import azeritePowerID
import os

azeritePowerIDs = azeritePowerID.azeritePowerIDs

parser = argparse.ArgumentParser(description='Analyzes a json file.')
parser.add_argument('dir', help='Directory you wish to analyze.')
parser.add_argument('--weights', help='For sims ran with weights this flag will change how analzye is ran.', action='store_true')
parser.add_argument('--talents', help='indicate talent build for output.', choices=['AS','SC'])
args = parser.parse_args()

csv = "%sresults/statweights.txt" % args.dir

if args.talents:
    outputMarkdown = "{0}Results_Dungeons_{1}.md".format(args.dir, args.talents)
    outputCSV = "{0}Results_Dungeons_{1}.csv".format(args.dir, args.talents)
    outputAPW = "{0}AzeritePowerWeights_Dungeons_{1}.md".format(args.dir, args.talents)
else:
    outputMarkdown = "%sREADME_Dungeons.md" % args.dir
    outputCSV = "%sresults_Dungeons.csv" % args.dir

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

if args.weights:
    data = pandas.read_csv(csv,usecols=['profile','actor','DD','DPS','int','haste','crit','mastery','vers'])
else:
    data = pandas.read_csv(csv,usecols=['profile','actor','DD','DPS'])

results = {}

# ['profile','actor','DD','DPS']
for value in data.iterrows():
    profile = value[1].profile
    if args.weights:
        haste = value[1].haste / value[1].int
        crit = value[1].crit / value[1].int
        mastery = value[1].mastery / value[1].int
        vers = value[1].vers / value[1].int
        wdps = 1 / value[1].int
        weight = 1
    weightedDPS = value[1].DPS
    if args.weights:
        results[value[1].actor] = [weightedDPS,weight,haste,crit,mastery,vers,wdps]
    else:
        results[value[1].actor] = weightedDPS

if args.dir == "talents/" or args.dir == "trinkets/" or args.dir == "azerite-gear/" or args.dir == "azerite-traits/" :
    baseDPS = results.get('Base') / 1
    results['Base'] = baseDPS
    # if args.dir == "azerite-gear/":
    #     # alter AS_Base dps
    #     baseDPSAS = results.get('Base_AS') / 3
    #     results['Base_AS'] = baseDPSAS
elif args.dir == "gear/":
    baseDPS = results.get('Priest_Shadow_T22M')
elif args.dir == "stats/":
    baseActor = results.get('Base')
    baseActor = [(baseActor[0] / 6),(baseActor[1] / 6),(baseActor[2] / 6),(baseActor[3] / 6),(baseActor[4] / 6),(baseActor[5] / 6),(baseActor[6] / 6)]
    results['Base'] = baseActor
else:
    baseDPS = results.get('Base')

# README.md output
with open(outputMarkdown, 'w') as resultsMD:
    # Uldir Composite
    if args.weights:
        resultsMD.write('# HeroDamage Dungeons\n| Actor | DPS | Int | Haste | Crit | Mastery | Vers | DPS Weight |\n|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n')
        for key, value in sorted(results.items(), key=operator.itemgetter(1), reverse=True):
            resultsMD.write("|%s|%.0f|%.2f|%.2f|%.2f|%.2f|%.2f|%.2f|\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5], value[6]))
    else:
        resultsMD.write('# HeroDamage Dungeons\n| Actor | DPS | Increase |\n|---|:---:|:---:|\n')
        for key, value in sorted(results.items(), key=operator.itemgetter(1), reverse=True):
            resultsMD.write("|%s|%.0f|%.2f%%|\n" % (key, value, getChange(value, baseDPS)))
    resultsMD.write('\n Dungeon sim profile courtesy of [HeroDamage](https://www.herodamage.com/)')

# results.csv output
with open(outputCSV, 'w') as resultsCSV:
    # HeroDamage Dungeons
    if args.weights:
        resultsCSV.write('profile,actor,DPS,int,haste,crit,mastery,vers,dpsW,\n')
        for key, value in sorted(results.items(), key=operator.itemgetter(1), reverse=True):
            resultsCSV.write("dungeons,%s,%.0f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5], value[6]))
    else:
        resultsCSV.write('profile,actor,DPS,increase,\n')
        for key, value in sorted(results.items(), key=operator.itemgetter(1), reverse=True):
            resultsCSV.write("dungeons,%s,%.0f,%.2f%%,\n" % (key, value, getChange(value, baseDPS)))

# AzeritePowerWeights Export
if args.dir == "azerite-traits/":
    with open(outputAPW, 'w') as resultsAPW:
        # HeroDamage Dungeons
        resultsAPW.write("# HeroDamage Dungeons\n```\n( AzeritePowerWeights:1:\"Priest - HeroDamage Dungeons {0}\":5:258:".format(args.talents))
        for key, value in sorted(results.items(), key=operator.itemgetter(1), reverse=True):
            traitID = azeritePowerIDs.get(key)
            if traitID:
                resultsAPW.write(" %s=%.2f," % (traitID, getChange(value, baseDPS)))
        resultsAPW.write(')\n```\n')
        resultsAPW.write('\n Works with the [AzeritePowerWeights Addon](https://wow.curseforge.com/projects/azeritepowerweights)')
        resultsAPW.write('\n Dungeon sim profile courtesy of [HeroDamage](https://www.herodamage.com/)')

# #Update JSONs
# import subprocess
# if args.dir == "trinkets/" or "azerite-traits/" or "azerite-gear/":
#     subprocess.call(['python', 'csvToJson.py'])
