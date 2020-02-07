import pandas
import weights
import argparse
import operator
import azeritePowerID
import os
import corruptionValues

azeritePowerIDs = azeritePowerID.azeritePowerIDs
weightsSingle = weights.weightsSingle
weightsNy = weights.weightsNy
corruptionValue = corruptionValues.corruptionValues

parser = argparse.ArgumentParser(description='Analyzes a json file.')
parser.add_argument('dir', help='Directory you wish to analyze.')
parser.add_argument('--weights', help='For sims ran with weights this flag will change how analzye is ran.', action='store_true')
parser.add_argument('--talents', help='indicate talent build for output.', choices=['AS','SC'])
args = parser.parse_args()

csv = "%sresults/statweights.txt" % args.dir

if args.talents:
    outputMarkdown = "{0}Results_{1}.md".format(args.dir, args.talents)
    outputCSV = "{0}Results_{1}.csv".format(args.dir, args.talents)
    outputAPW = "{0}AzeritePowerWeights_{1}.md".format(args.dir, args.talents)
    outputCorruptionMD = "{0}Corruption_Value_Results_{1}.md".format(args.dir, args.talents)
    outputCorruptionCSV = "{0}Corruption_Value_Results_{1}.csv".format(args.dir, args.talents)
else:
    outputMarkdown = "%sREADME.md" % args.dir
    outputCSV = "%sresults.csv" % args.dir

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

def getCorruptionValue(baseDPS, newDPS, corruptionValue):
    delta = newDPS - baseDPS
    if delta < 0:
        return 0
    elif corruptionValue is None:
        return 0
    try:
        return delta / corruptionValue
    except Exception as e:
        return 0

if args.weights:
    data = pandas.read_csv(csv,usecols=['profile','actor','DD','DPS','int','haste','crit','mastery','vers'])
else:
    data = pandas.read_csv(csv,usecols=['profile','actor','DD','DPS'])

results = {}
resultsSingle = {}
corruptionResults = {}
corruptionResultsSingle = {}

# ['profile','actor','DD','DPS']
for value in data.iterrows():
    if args.weights:
        profile = value[1].profile
        weight = weightsNy.get(profile[profile.index('_')+1:])
        weightSingle = weightsSingle.get(profile[profile.index('_')+1:])
        haste = (value[1].haste / value[1].int) * weight
        crit = (value[1].crit / value[1].int) * weight
        mastery = (value[1].mastery / value[1].int) * weight
        vers = (value[1].vers / value[1].int) * weight
        wdps = (1 / value[1].int) * weight
        if weightSingle:
            hasteSingle = (value[1].haste / value[1].int) * weightSingle
            critSingle = (value[1].crit / value[1].int) * weightSingle
            masterySingle = (value[1].mastery / value[1].int) * weightSingle
            versSingle = (value[1].vers / value[1].int) * weightSingle
            wdpsSingle = (1 / value[1].int) * weightSingle
    else:
        if args.dir == "talents/" or args.dir == "trinkets/" or args.dir == "azerite-gear/" or args.dir == "azerite-traits/" :
            profile = value[1].profile
            weight = weightsNy.get(profile[profile.index('_')+1:])
            weightSingle = weightsSingle.get(profile[profile.index('_')+1:])
        else:
            weight = weightsNy.get(value[1].profile)
            weightSingle = weightsSingle.get(value[1].profile)
    if not weightSingle:
        weightSingle = 0
        if args.weights:
            hasteSingle = 0
            critSingle = 0
            masterySingle = 0
            versSingle = 0
            wdpsSingle = 0
    weightedDPS = weight * value[1].DPS
    weightedDPSSingle = weightSingle * value[1].DPS
    if value[1].actor in results:
        if args.weights:
            existing = results.get(value[1].actor)
            results[value[1].actor] = [existing[0] + weightedDPS,existing[1] + weight,existing[2] + haste,existing[3] + crit,existing[4] + mastery,existing[5] + vers,existing[6] + wdps,]
        else:
            results[value[1].actor] = results.get(value[1].actor) + weightedDPS
    else:
        if args.weights:
            results[value[1].actor] = [weightedDPS,weight,haste,crit,mastery,vers,wdps]
        else:
            results[value[1].actor] = weightedDPS
    if value[1].actor in resultsSingle:
        if args.weights:
            existing = resultsSingle.get(value[1].actor)
            resultsSingle[value[1].actor] = [existing[0] + weightedDPSSingle,existing[1] + weightSingle,existing[2] + hasteSingle,existing[3] + critSingle,existing[4] + masterySingle,existing[5] + versSingle,existing[6] + wdpsSingle,]
        else:
            resultsSingle[value[1].actor] = resultsSingle.get(value[1].actor) + weightedDPSSingle
    else:
        if args.weights:
            resultsSingle[value[1].actor] = [weightedDPSSingle,weightSingle,hasteSingle,critSingle,masterySingle,versSingle,wdpsSingle]
        else:
            resultsSingle[value[1].actor] = weightedDPSSingle

if args.dir == "talents/" or args.dir == "trinkets/" or args.dir == "azerite-gear/" or args.dir == "azerite-traits/":
    baseDPS = results.get('Base') / 3
    results['Base'] = baseDPS
    baseDPSSingle = resultsSingle.get('Base') / 3
    resultsSingle['Base'] = baseDPSSingle
    # if args.dir == "azerite-gear/":
    #     # alter AS_Base dps
    #     baseDPSAS = results.get('Base_AS') / 3
    #     results['Base_AS'] = baseDPSAS
    #     baseDPSSingleAS = resultsSingle.get('Base_AS') / 3
    #     resultsSingle['Base_AS'] = baseDPSSingleAS
elif args.dir == "gear/":
    baseDPS = results.get('Priest_Shadow_T23M')
    baseDPSSingle = resultsSingle.get('Priest_Shadow_T23M')
elif args.dir == "stats/":
    baseActor = results.get('Base')
    baseActorSingle = resultsSingle.get('Base')
    baseActor = [(baseActor[0] / 6),(baseActor[1] / 6),(baseActor[2] / 6),(baseActor[3] / 6),(baseActor[4] / 6),(baseActor[5] / 6),(baseActor[6] / 6)]
    baseActorSingle = [(baseActorSingle[0] / 6),(baseActorSingle[1] / 6),(baseActorSingle[2] / 6),(baseActorSingle[3] / 6),(baseActorSingle[4] / 6),(baseActorSingle[5] / 6),(baseActorSingle[6] / 6)]
    results['Base'] = baseActor
    resultsSingle['Base'] = baseActorSingle
else:
    baseDPS = results.get('Base')
    baseDPSSingle = resultsSingle.get('Base')

# Corruption DPS MD
if args.dir == "corruption/":
    for key, value in sorted(results.items(), key=operator.itemgetter(1), reverse=True):
        corrValue = corruptionValue.get(key)
        if corrValue is None: corrValue = 0
        corruptionResults[key] = getCorruptionValue(baseDPS, value, corrValue)
    for key, value in sorted(resultsSingle.items(), key=operator.itemgetter(1), reverse=True):
        corrValue = corruptionValue.get(key)
        if corrValue is None: corrValue = 0
        corruptionResultsSingle[key] = getCorruptionValue(baseDPSSingle, value, corrValue)

# README.md output
with open(outputMarkdown, 'w') as resultsMD:
    # Ny'alotha Composite
    if args.weights:
        resultsMD.write('# Ny\'alotha\n| Actor | DPS | Int | Haste | Crit | Mastery | Vers | DPS Weight |\n|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n')
        for key, value in sorted(results.items(), key=operator.itemgetter(1), reverse=True):
            resultsMD.write("|%s|%.0f|%.2f|%.2f|%.2f|%.2f|%.2f|%.2f|\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5], value[6]))
    else:
        resultsMD.write('# Ny\'alotha\n| Actor | DPS | Increase |\n|---|:---:|:---:|\n')
        for key, value in sorted(results.items(), key=operator.itemgetter(1), reverse=True):
            resultsMD.write("|%s|%.0f|%.2f%%|\n" % (key, value, getChange(value, baseDPS)))
    # Single Target
    if args.weights:
        resultsMD.write('# Single Target\n| Actor | DPS | Int | Haste | Crit | Mastery | Vers | DPS Weight |\n|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n')
        for key, value in sorted(resultsSingle.items(), key=operator.itemgetter(1), reverse=True):
            resultsMD.write("|%s|%.0f|%.2f|%.2f|%.2f|%.2f|%.2f|%.2f|\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5], value[6]))
    else:
        resultsMD.write('\n# Single Target\n| Actor | DPS | Increase |\n|---|:---:|:---:|\n')
        for key, value in sorted(resultsSingle.items(), key=operator.itemgetter(1), reverse=True):
            resultsMD.write("|%s|%.0f|%.2f%%|\n" % (key, value, getChange(value, baseDPSSingle)))

# Corruption DPS MD
if args.dir == "corruption/":
    with open(outputCorruptionMD, 'w') as resultsMD:
        resultsMD.write('# Ny\'alotha\n| Actor | DPS | Corruption | Value |\n|---|:---:|:---:|:---:|\n')
        for key, value in sorted(corruptionResults.items(), key=operator.itemgetter(1), reverse=True):
            dpsValue = results.get(key)
            corrValue = corruptionValue.get(key)
            if corrValue is None: corrValue = 0
            resultsMD.write("|%s|%.0f|%.0f|%.2f|\n" % (key, dpsValue, corrValue, value))
        resultsMD.write('\n# Single Target\n| Actor | DPS | Corruption | Value |\n|---|:---:|:---:|:---:|\n')
        for key, value in sorted(corruptionResultsSingle.items(), key=operator.itemgetter(1), reverse=True):
            dpsValue = resultsSingle.get(key)
            corrValue = corruptionValue.get(key)
            if corrValue is None: corrValue = 0
            resultsMD.write("|%s|%.0f|%.0f|%.2f|\n" % (key, dpsValue, corrValue, value))

# results.csv output
with open(outputCSV, 'w') as resultsCSV:
    # Ny'alothaBattle for Dazar'alor Composite
    if args.weights:
        resultsCSV.write('profile,actor,DPS,int,haste,crit,mastery,vers,dpsW,\n')
        for key, value in sorted(results.items(), key=operator.itemgetter(1), reverse=True):
            resultsCSV.write("composite,%s,%.0f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5], value[6]))
    else:
        resultsCSV.write('profile,actor,DPS,increase,\n')
        for key, value in sorted(results.items(), key=operator.itemgetter(1), reverse=True):
            resultsCSV.write("composite,%s,%.0f,%.2f%%,\n" % (key, value, getChange(value, baseDPS)))
    # Single Target
    if args.weights:
        for key, value in sorted(resultsSingle.items(), key=operator.itemgetter(1), reverse=True):
            resultsCSV.write("single_target,%s,%.0f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5], value[6]))
    else:
        for key, value in sorted(resultsSingle.items(), key=operator.itemgetter(1), reverse=True):
            resultsCSV.write("single_target,%s,%.0f,%.2f%%,\n" % (key, value, getChange(value, baseDPSSingle)))

# Corruption DPS CSV
if args.dir == "corruption/":
    with open(outputCorruptionCSV, 'w') as resultsCSV:
        resultsCSV.write('profile,actor,DPS,corruption,value,\n')
        for key, value in sorted(corruptionResults.items(), key=operator.itemgetter(1), reverse=True):
            dpsValue = results.get(key)
            corrValue = corruptionValue.get(key)
            if corrValue is None: corrValue = 0
            resultsCSV.write("composite,%s,%.0f,%.0f,%.2f%%,\n" % (key, dpsValue, corrValue, value))
        for key, value in sorted(corruptionResultsSingle.items(), key=operator.itemgetter(1), reverse=True):
            dpsValue = resultsSingle.get(key)
            corrValue = corruptionValue.get(key)
            if corrValue is None: corrValue = 0
            resultsCSV.write("single_target,%s,%.0f,%.0f,%.2f%%,\n" % (key, dpsValue, corrValue, value))

# AzeritePowerWeights Export
if args.dir == "azerite-traits/":
    with open(outputAPW, 'w') as resultsAPW:
        # Battle for Dazar'alor Composite
        resultsAPW.write("# Ny'alotha\n```\n( AzeritePowerWeights:1:\"Priest - Ny'alotha Composite {0}\":5:258:".format(args.talents))
        for key, value in sorted(results.items(), key=operator.itemgetter(1), reverse=True):
            traitID = azeritePowerIDs.get(key)
            if traitID:
                resultsAPW.write(" %s=%.2f," % (traitID, getChange(value, baseDPS)))
        resultsAPW.write(')\n```\n')
        # Single Target
        resultsAPW.write("# Single Target\n```\n( AzeritePowerWeights:1:\"Priest - Single Target {0}\":5:258:".format(args.talents))
        for key, value in sorted(resultsSingle.items(), key=operator.itemgetter(1), reverse=True):
            traitID = azeritePowerIDs.get(key)
            if traitID:
                resultsAPW.write(" %s=%.2f," % (traitID, getChange(value, baseDPSSingle)))
        resultsAPW.write(')\n```\n')
        resultsAPW.write('\n Works with the [AzeritePowerWeights Addon](https://wow.curseforge.com/projects/azeritepowerweights)')

#Update JSONs
import subprocess
if args.dir == "trinkets/" or "azerite-traits/" or "azerite-gear/":
    subprocess.call(['python', 'csvToJson.py'])
