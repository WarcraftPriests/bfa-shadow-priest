import pandas
import weights
import argparse

weightsSingle = weights.weightsSingle
weightsATBT = weights.weightsATBT

parser = argparse.ArgumentParser(description='Analyzes a json file.')
parser.add_argument('dir', help='Directory you wish to analyze.')
parser.add_argument('--weights', help='For sims ran with weights this flag will change how analzye is ran.', action='store_true')
args = parser.parse_args()

csv = "%sresults/statweights.txt" % args.dir
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

if args.weights:
    data = pandas.read_csv(csv,usecols=['profile','actor','DD','DPS','int','haste','crit','mastery','vers'])
else:
    data = pandas.read_csv(csv,usecols=['profile','actor','DD','DPS'])

results = {}
resultsSingle = {}

# ['profile','actor','DD','DPS']
for value in data.iterrows():
    if args.weights:
        profile = value[1].profile
        weight = weightsATBT.get(profile[profile.index('_')+1:])
        weightSingle = weightsSingle.get(profile[profile.index('_')+1:])
        haste = (value[1].haste / value[1].int) * weight
        crit = (value[1].crit / value[1].int) * weight
        mastery = (value[1].mastery / value[1].int) * weight
        vers = (value[1].vers / value[1].int) * weight
        if weightSingle:
            hasteSingle = (value[1].haste / value[1].int) * weightSingle
            critSingle = (value[1].crit / value[1].int) * weightSingle
            masterySingle = (value[1].mastery / value[1].int) * weightSingle
            versSingle = (value[1].vers / value[1].int) * weightSingle
    else:
        if args.dir == "talents/" or args.dir == "trinkets/":
            profile = value[1].profile
            weight = weightsATBT.get(profile[profile.index('_')+1:])
            weightSingle = weightsSingle.get(profile[profile.index('_')+1:])
        else:
            weight = weightsATBT.get(value[1].profile)
            weightSingle = weightsSingle.get(value[1].profile)
    if not weightSingle:
        weightSingle = 0
        if args.weights:
            hasteSingle = 0
            critSingle = 0
            masterySingle = 0
            versSingle = 0
    weightedDPS = weight * value[1].DPS
    weightedDPSSingle = weightSingle * value[1].DPS
    if value[1].actor in results:
        if args.weights:
            existing = results.get(value[1].actor)
            results[value[1].actor] = [existing[0] + weightedDPS,existing[1] + weight,existing[2] + haste,existing[3] + crit,existing[4] + mastery,existing[5] + vers,]
        else:
            results[value[1].actor] = results.get(value[1].actor) + weightedDPS
    else:
        if args.weights:
            results[value[1].actor] = [weightedDPS,weight,haste,crit,mastery,vers]
        else:
            results[value[1].actor] = weightedDPS
    if value[1].actor in resultsSingle:
        if args.weights:
            existing = resultsSingle.get(value[1].actor)
            resultsSingle[value[1].actor] = [existing[0] + weightedDPSSingle,existing[1] + weightSingle,existing[2] + hasteSingle,existing[3] + critSingle,existing[4] + masterySingle,existing[5] + versSingle,]
        else:
            resultsSingle[value[1].actor] = resultsSingle.get(value[1].actor) + weightedDPSSingle
    else:
        if args.weights:
            resultsSingle[value[1].actor] = [weightedDPSSingle,weightSingle,hasteSingle,critSingle,masterySingle,versSingle]
        else:
            resultsSingle[value[1].actor] = weightedDPSSingle

if args.dir == "talents/" or args.dir == "trinkets/":
    baseDPS = results.get('Base') / 3
    results['Base'] = baseDPS
    baseDPSSingle = resultsSingle.get('Base') / 3
    resultsSingle['Base'] = baseDPSSingle
elif args.dir == "gear/":
    baseDPS = results.get('Priest_Shadow_T22N')
    baseDPSSingle = resultsSingle.get('Priest_Shadow_T22N')
    if not baseDPS:
        baseDPS = results.get('Priest_Shadow_T22H')
        baseDPSSingle = resultsSingle.get('Priest_Shadow_T22H')
        if not baseDPS:
            baseDPS = results.get('Priest_Shadow_T22M')
            baseDPSSingle = resultsSingle.get('Priest_Shadow_T22M')
else:
    baseDPS = results.get('Base')
    baseDPSSingle = resultsSingle.get('Base')

# README.md output
with open(outputMarkdown, 'w') as resultsMD:
    # Antorus Composite
    if args.weights:
        resultsMD.write('# Antorus Composite\n| Actor | DPS | Int | Haste | Crit | Mastery | Vers |\n|---|:---:|:---:|:---:|:---:|:---:|:---:|\n')
        for key, value in results.items():
            resultsMD.write("|%s|%.0f|%.2f|%.2f|%.2f|%.2f|%.2f|\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5]))
    else:
        resultsMD.write('# Antorus Composite\n| Actor | DPS | Increase |\n|---|:---:|:---:|\n')
        for key, value in sorted(results.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsMD.write("|%s|%.0f|%.2f%%|\n" % (key, value, getChange(value, baseDPS)))
    # Single Target
    if args.weights:
        resultsMD.write('# Single Target\n| Actor | DPS | Int | Haste | Crit | Mastery | Vers |\n|---|:---:|:---:|:---:|:---:|:---:|:---:|\n')
        for key, value in resultsSingle.items():
            resultsMD.write("|%s|%.0f|%.2f|%.2f|%.2f|%.2f|%.2f|\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5]))
    else:
        resultsMD.write('\n# Single Target\n| Actor | DPS | Increase |\n|---|:---:|:---:|\n')
        for key, value in sorted(resultsSingle.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsMD.write("|%s|%.0f|%.2f%%|\n" % (key, value, getChange(value, baseDPSSingle)))

# results.csv output
with open(outputCSV, 'w') as resultsCSV:
    # Antorus Composite
    if args.weights:
        resultsCSV.write('profile,actor,DPS,int,haste,crit,mastery,vers,\n')
        for key, value in results.items():
            resultsCSV.write("composite,%s,%.0f,%.2f,%.2f,%.2f,%.2f,%.2f,\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5]))
    else:
        resultsCSV.write('profile,actor,DPS,increase,\n')
        for key, value in sorted(results.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsCSV.write("composite,%s,%.0f,%.2f%%,\n" % (key, value, getChange(value, baseDPS)))
    # Single Target
    if args.weights:
        for key, value in resultsSingle.items():
            resultsCSV.write("single_target,%s,%.0f,%.2f,%.2f,%.2f,%.2f,%.2f,\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5]))
    else:
        for key, value in sorted(resultsSingle.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsCSV.write("single_target,%s,%.0f,%.2f%%,\n" % (key, value, getChange(value, baseDPSSingle)))
