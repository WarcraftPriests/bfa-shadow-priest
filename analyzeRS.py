import pandas
import weights
import argparse
import re

parser = argparse.ArgumentParser(description='Analyzes a json file.')
parser.add_argument('dir', help='Directory you wish to analyze.')
parser.add_argument('--weights', help='For sims ran with weights this flag will change how analzye is ran.', action='store_true')
parser.add_argument('--composite', help='Analyze a raidsimming batch of sims. Value can be either HH or MM.', choices=['HC','MM'])
args = parser.parse_args()

csv = "%sresults/statweights.txt" % args.dir
outputMarkdownRS = "{0}RaidSimming_{1}.md".format(args.dir, args.composite)
outputCSVRS = "{0}RaidSimming_{1}.csv".format(args.dir, args.composite)

if args.composite == "HC":
    weights = weights.weightsUldirHC
else:
    weights = weights.weightsUldirMM

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
taloc = {}
mother = {}
fetid = {}
zekvoz = {}
vectis = {}
zul = {}
mythrax = {}
ghuun = {}

# ['profile','actor','DD','DPS']
for value in data.iterrows():
    profile = value[1].profile
    if args.weights or args.dir == "talents/" or args.dir == "trinkets/":
        # HC_da1_FetidDevourer -> HC_FetidDevourer
        # HC_da_FetidDevourer -> HC_FetidDevourer
        profile = re.sub(r"(_\w*?_)", "_", profile)
    if args.weights:
        weight = weights.get(profile)
        if value[1].int <= 0:
            value[1].int = 0.01
        haste = (value[1].haste / value[1].int) * weight
        crit = (value[1].crit / value[1].int) * weight
        mastery = (value[1].mastery / value[1].int) * weight
        vers = (value[1].vers / value[1].int) * weight
    else:
        # if args.dir == "talents/" or args.dir == "trinkets/":
        #     weight = weights.get(profile)
        # else:
        weight = weights.get(profile)
    weightedDPS = weight * value[1].DPS
    # calculate composite
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
    if args.weights:
        if profile == "HC_Taloc":
            taloc[value[1].actor] = [value[1].DPS,1.00,value[1].haste,value[1].crit,value[1].mastery,value[1].vers]
        elif profile == "HC_Mother_Early" or profile == "HC_Mother_Late":
            if value[1].actor in mother:
                existing = mother.get(value[1].actor)
                mother[value[1].actor] = [existing[0] + (value[1].DPS * .5),existing[1] + 0.5,existing[2] + (value[1].haste * .5),existing[3] + (value[1].crit * .5),existing[4] + (value[1].mastery * .5),existing[5] + (value[1].vers * .5)]
            else:
                mother[value[1].actor] = [(value[1].DPS * .5),0.5,(value[1].haste * .5),(value[1].crit * .5),(value[1].mastery * .5),(value[1].vers * .5)]
        if profile == "HC_FetidDevourer":
            fetid[value[1].actor] = [value[1].DPS,1.00,value[1].haste,value[1].crit,value[1].mastery,value[1].vers]
        if profile == "HC_Zekvoz":
            zekvoz[value[1].actor] = [value[1].DPS,1.00,value[1].haste,value[1].crit,value[1].mastery,value[1].vers]
        if profile == "HC_Vectis":
            vectis[value[1].actor] = [value[1].DPS,1.00,value[1].haste,value[1].crit,value[1].mastery,value[1].vers]
        if profile == "HC_Zul":
            zul[value[1].actor] = [value[1].DPS,1.00,value[1].haste,value[1].crit,value[1].mastery,value[1].vers]
        if profile == "HC_Mythrax":
            mythrax[value[1].actor] = [value[1].DPS,1.00,value[1].haste,value[1].crit,value[1].mastery,value[1].vers]
        if profile == "HC_Ghuun":
            ghuun[value[1].actor] = [value[1].DPS,1.00,value[1].haste,value[1].crit,value[1].mastery,value[1].vers]
    else:
        if profile == "HC_Taloc":
            taloc[value[1].actor] = value[1].DPS
        elif profile == "HC_Mother_Early" or profile == "HC_Mother_Late":
            if value[1].actor in mother:
                mother[value[1].actor] = mother.get(value[1].actor) + (value[1].DPS * .5)
            else:
                mother[value[1].actor] = (value[1].DPS * .5)
        if profile == "HC_FetidDevourer":
            fetid[value[1].actor] = value[1].DPS
        if profile == "HC_Zekvoz":
            zekvoz[value[1].actor] = value[1].DPS
        if profile == "HC_Vectis":
            vectis[value[1].actor] = value[1].DPS
        if profile == "HC_Zul":
            zul[value[1].actor] = value[1].DPS
        if profile == "HC_Mythrax":
            mythrax[value[1].actor] = value[1].DPS
        if profile == "HC_Ghuun":
            ghuun[value[1].actor] = value[1].DPS

if args.dir == "talents/" or args.dir == "trinkets/":
    baseDPS = results.get('Base') / 3
    baseTaloc = taloc.get('Base')
    baseMother = mother.get('Base')
    baseFetid = fetid.get('Base')
    baseZekvoz = zekvoz.get('Base')
    baseVectis = vectis.get('Base')
    baseZul = zul.get('Base')
    # baseMythrax = mythrax.get('Base')
    baseMythrax = 0
    baseGhuun = ghuun.get('Base')
    results['Base'] = baseDPS
elif args.dir == "gear/":
    baseDPS = results.get('Priest_Shadow_T22N')
    baseTaloc = taloc.get('Priest_Shadow_T22N')
    baseMother = mother.get('Priest_Shadow_T22N')
    baseFetid = fetid.get('Priest_Shadow_T22N')
    baseZekvoz = zekvoz.get('Priest_Shadow_T22N')
    baseVectis = vectis.get('Priest_Shadow_T22N')
    baseZul = zul.get('Priest_Shadow_T22N')
    baseMythrax = mythrax.get('Priest_Shadow_T22N')
    baseGhuun = ghuun.get('Priest_Shadow_T22N')
    if not baseDPS:
        baseDPS = results.get('Priest_Shadow_T22H')
        baseTaloc = taloc.get('Priest_Shadow_T22H')
        baseMother = mother.get('Priest_Shadow_T22H')
        baseFetid = fetid.get('Priest_Shadow_T22H')
        baseZekvoz = zekvoz.get('Priest_Shadow_T22H')
        baseVectis = vectis.get('Priest_Shadow_T22H')
        baseZul = zul.get('Priest_Shadow_T22H')
        baseMythrax = mythrax.get('Priest_Shadow_T22H')
        baseGhuun = ghuun.get('Priest_Shadow_T22H')
        if not baseDPS:
            baseDPS = results.get('Priest_Shadow_T22M')
            baseTaloc = taloc.get('Priest_Shadow_T22M')
            baseMother = mother.get('Priest_Shadow_T22M')
            baseFetid = fetid.get('Priest_Shadow_T22M')
            baseZekvoz = zekvoz.get('Priest_Shadow_T22M')
            baseVectis = vectis.get('Priest_Shadow_T22M')
            baseZul = zul.get('Priest_Shadow_T22M')
            baseMythrax = mythrax.get('Priest_Shadow_T22M')
            baseGhuun = ghuun.get('Priest_Shadow_T22M')
else:
    baseDPS = results.get('Base')
    baseTaloc = taloc.get('Base')
    baseMother = mother.get('Base')
    baseFetid = fetid.get('Base')
    baseZekvoz = zekvoz.get('Base')
    baseVectis = vectis.get('Base')
    baseZul = zul.get('Base')
    baseMythrax = mythrax.get('Base')
    baseGhuun = ghuun.get('Base')

# README.md output
with open(outputMarkdownRS, 'w') as resultsMD:
    # Uldir Raidsimming
    if args.weights:
        resultsMD.write('# Composite\n| Actor | DPS | Int | Haste | Crit | Mastery | Vers |\n|---|:---:|:---:|:---:|:---:|:---:|:---:|\n')
        for key, value in results.items():
            resultsMD.write("|%s|%.0f|%.2f|%.2f|%.2f|%.2f|%.2f|\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5]))

        resultsMD.write('# Taloc\n| Actor | DPS | Int | Haste | Crit | Mastery | Vers |\n|---|:---:|:---:|:---:|:---:|:---:|:---:|\n')
        for key, value in taloc.items():
            resultsMD.write("|%s|%.0f|%.2f|%.2f|%.2f|%.2f|%.2f|\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5]))

        resultsMD.write('# Mother\n| Actor | DPS | Int | Haste | Crit | Mastery | Vers |\n|---|:---:|:---:|:---:|:---:|:---:|:---:|\n')
        for key, value in mother.items():
            resultsMD.write("|%s|%.0f|%.2f|%.2f|%.2f|%.2f|%.2f|\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5]))

        resultsMD.write('# Fetid\n| Actor | DPS | Int | Haste | Crit | Mastery | Vers |\n|---|:---:|:---:|:---:|:---:|:---:|:---:|\n')
        for key, value in fetid.items():
            resultsMD.write("|%s|%.0f|%.2f|%.2f|%.2f|%.2f|%.2f|\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5]))

        resultsMD.write('# Zekvoz\n| Actor | DPS | Int | Haste | Crit | Mastery | Vers |\n|---|:---:|:---:|:---:|:---:|:---:|:---:|\n')
        for key, value in zekvoz.items():
            resultsMD.write("|%s|%.0f|%.2f|%.2f|%.2f|%.2f|%.2f|\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5]))

        resultsMD.write('# Vectis\n| Actor | DPS | Int | Haste | Crit | Mastery | Vers |\n|---|:---:|:---:|:---:|:---:|:---:|:---:|\n')
        for key, value in vectis.items():
            resultsMD.write("|%s|%.0f|%.2f|%.2f|%.2f|%.2f|%.2f|\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5]))

        resultsMD.write('# Zul\n| Actor | DPS | Int | Haste | Crit | Mastery | Vers |\n|---|:---:|:---:|:---:|:---:|:---:|:---:|\n')
        for key, value in zul.items():
            resultsMD.write("|%s|%.0f|%.2f|%.2f|%.2f|%.2f|%.2f|\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5]))

        resultsMD.write('# Mythrax\n| Actor | DPS | Int | Haste | Crit | Mastery | Vers |\n|---|:---:|:---:|:---:|:---:|:---:|:---:|\n')
        for key, value in mythrax.items():
            resultsMD.write("|%s|%.0f|%.2f|%.2f|%.2f|%.2f|%.2f|\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5]))

        resultsMD.write('# Ghuun\n| Actor | DPS | Int | Haste | Crit | Mastery | Vers |\n|---|:---:|:---:|:---:|:---:|:---:|:---:|\n')
        for key, value in ghuun.items():
            resultsMD.write("|%s|%.0f|%.2f|%.2f|%.2f|%.2f|%.2f|\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5]))
    else:
        resultsMD.write('# Composite\n| Actor | DPS | Increase |\n|---|:---:|:---:|\n')
        for key, value in sorted(results.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsMD.write("|%s|%.0f|%.2f%%|\n" % (key, value, getChange(value, baseDPS)))

        resultsMD.write('# Taloc\n| Actor | DPS | Increase |\n|---|:---:|:---:|\n')
        for key, value in sorted(taloc.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsMD.write("|%s|%.0f|%.2f%%|\n" % (key, value, getChange(value, baseTaloc)))

        resultsMD.write('# Mother\n| Actor | DPS | Increase |\n|---|:---:|:---:|\n')
        for key, value in sorted(mother.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsMD.write("|%s|%.0f|%.2f%%|\n" % (key, value, getChange(value, baseMother)))

        resultsMD.write('# Fetid\n| Actor | DPS | Increase |\n|---|:---:|:---:|\n')
        for key, value in sorted(fetid.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsMD.write("|%s|%.0f|%.2f%%|\n" % (key, value, getChange(value, baseFetid)))

        resultsMD.write('# Zekvoz\n| Actor | DPS | Increase |\n|---|:---:|:---:|\n')
        for key, value in sorted(zekvoz.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsMD.write("|%s|%.0f|%.2f%%|\n" % (key, value, getChange(value, baseZekvoz)))

        resultsMD.write('# Vectis\n| Actor | DPS | Increase |\n|---|:---:|:---:|\n')
        for key, value in sorted(vectis.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsMD.write("|%s|%.0f|%.2f%%|\n" % (key, value, getChange(value, baseVectis)))

        resultsMD.write('# Zul\n| Actor | DPS | Increase |\n|---|:---:|:---:|\n')
        for key, value in sorted(zul.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsMD.write("|%s|%.0f|%.2f%%|\n" % (key, value, getChange(value, baseZul)))

        resultsMD.write('# Mythrax\n| Actor | DPS | Increase |\n|---|:---:|:---:|\n')
        for key, value in sorted(mythrax.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsMD.write("|%s|%.0f|%.2f%%|\n" % (key, value, getChange(value, baseMythrax)))

        resultsMD.write('# G\'huun\n| Actor | DPS | Increase |\n|---|:---:|:---:|\n')
        for key, value in sorted(ghuun.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsMD.write("|%s|%.0f|%.2f%%|\n" % (key, value, getChange(value, baseGhuun)))

with open(outputCSVRS, 'w') as resultsCSV:
    # Uldir Raidsimming
    if args.weights:
        resultsCSV.write('profile,actor,DPS,int,haste,crit,mastery,vers,\n')
        for key, value in results.items():
            resultsCSV.write("composite,%s,%.0f,%.2f,%.2f,%.2f,%.2f,%.2f,\n" % (key, value[0], value[1], value[2], value[3], value[4], value[5]))
    else:
        resultsCSV.write('profile,actor,DPS,increase,\n')
        for key, value in sorted(results.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsCSV.write("composite,%s,%.0f,%.2f%%,\n" % (key, value, getChange(value, baseDPS)))
        for key, value in sorted(taloc.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsCSV.write("taloc,%s,%.0f,%.2f%%,\n" % (key, value, getChange(value, baseTaloc)))
        for key, value in sorted(mother.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsCSV.write("mother,%s,%.0f,%.2f%%,\n" % (key, value, getChange(value, baseMother)))
        for key, value in sorted(fetid.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsCSV.write("fetid,%s,%.0f,%.2f%%,\n" % (key, value, getChange(value, baseFetid)))
        for key, value in sorted(zekvoz.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsCSV.write("zekvoz,%s,%.0f,%.2f%%,\n" % (key, value, getChange(value, baseZekvoz)))
        for key, value in sorted(vectis.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsCSV.write("vectis,%s,%.0f,%.2f%%,\n" % (key, value, getChange(value, baseVectis)))
        for key, value in sorted(zul.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsCSV.write("zul,%s,%.0f,%.2f%%,\n" % (key, value, getChange(value, baseZul)))
        for key, value in sorted(mythrax.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsCSV.write("mythrax,%s,%.0f,%.2f%%,\n" % (key, value, getChange(value, baseMythrax)))
        for key, value in sorted(ghuun.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            resultsCSV.write("ghuun,%s,%.0f,%.2f%%,\n" % (key, value, getChange(value, baseGhuun)))
