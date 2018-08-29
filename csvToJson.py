import csv
import json
import re
import time
import os

starttime = time.time()

#Define all file paths
#Trinkets
trinketsDA = os.path.os.path.abspath(os.path.join(os.getcwd(), 'trinkets/Results_DA.csv'))
trinketsLotV = os.path.os.path.abspath(os.path.join(os.getcwd(), 'trinkets/Results_LotV.csv'))

#Triats
traitsDA = os.path.os.path.abspath(os.path.join(os.getcwd(), 'azerite-traits/Results_DA.csv'))
traitsLotV = os.path.os.path.abspath(os.path.join(os.getcwd(), 'azerite-traits/Results_LotV.csv'))

#JSON Files
#Trinkets
trinketsDAJson = os.path.os.path.abspath(os.path.join(os.getcwd(), 'trinkets/Results_DA.json'))
trinketsLotVJson = os.path.os.path.abspath(os.path.join(os.getcwd(), 'trinkets/Results_LotV.json'))
#Traits
traitsDAJson = os.path.os.path.abspath(os.path.join(os.getcwd(), 'azerite-traits/Results_DA.json'))
traitsLotVJson = os.path.os.path.abspath(os.path.join(os.getcwd(), 'azerite-traits/Results_LotV.json'))

# SimC files
trinketsDungeonsDA = os.path.os.path.abspath(os.path.join(os.getcwd(), 'trinkets/trinkets_dungeons_DA.simc'))
trinketsOtherDA = os.path.os.path.abspath(os.path.join(os.getcwd(), 'trinkets/trinkets_other_DA.simc'))
trinketsRaidDA = os.path.os.path.abspath(os.path.join(os.getcwd(), 'trinkets/trinkets_raid_DA.simc'))

#CSV Field names
fieldnames = ('profile', 'actor', 'DPS', 'increase')

def parseCSV(file, json_file):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        field = reader.fieldnames
        for row in reader:
            csv_rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        csvToJson(csv_rows, json_file)

def csvToJson(data, json_file):
    with open(json_file, "w") as f:
        f.write(json.dumps(data, sort_keys=False, indent=2, separators=(',', ': ')))


parseCSV(trinketsDA,trinketsDAJson)
parseCSV(trinketsLotV,trinketsLotVJson)
parseCSV(traitsDA,traitsDAJson)
parseCSV(traitsLotV,traitsLotVJson)


def getItemId(itemname):
    itemname = itemname.lower().rstrip()
    with open(trinketsDungeonsDA, 'r') as f:
        lines = f.readlines()
        for line in lines:
            try:
                if re.search(r'(trinket1=)\D*',line).group(0).replace('trinket1=','').replace(',id=','') == itemname:
                    itemID = re.search(r'(id=)\d*',line.strip('\n')).group(0).strip('id=')
                    return itemID
            except:
                continue
    with open(trinketsOtherDA, 'r') as f:
        lines = f.readlines()
        for line in lines:
            try:
                if re.search(r'(trinket1=)\D*',line).group(0).replace('trinket1=','').replace(',id=','') == itemname:
                    itemID = re.search(r'(id=)\d*',line).group(0).strip('id=')
                    return itemID
            except:
                continue
    with open(trinketsRaidDA, 'r') as f:
        lines = f.readlines()
        for line in lines:
            try:
                if re.search(r'(trinket1=)\D*',line).group(0).replace('trinket1=','').replace(',id=','') == itemname:
                    itemID = re.search(r'(id=)\d*',line).group(0).strip('id=')
                    return itemID
            except:
                continue


def make_unique(original_list):
    unique_list = []
    [unique_list.append(obj) for obj in original_list if obj not in unique_list]
    return unique_list

def getNames(jsonFile):
	with open(jsonFile,'r') as f:
		nameList = list()
		data = json.load(f)
		for x in data:
			m = re.search(r"\D*",x['actor']).group(0).replace('_',' ').rstrip()
			nameList.append(m)
		uniqueList = make_unique(nameList)
	return uniqueList

def getIlvl(jsonFile):
    with open(jsonFile,'r') as f:
        nameList = list()
        data = json.load(f)
        for x in data:
            m = re.search(r"\d*",x['actor'].lstrip().split('_')[-1]).group(0)
            nameList.append(m)
        uniqueList = make_unique(nameList)
    return uniqueList

def addNamesToJson(jsonFile):
	names = getNames(jsonFile)
	with open(jsonFile, 'r+') as f:
		data = json.load(f)
		data.append(names)
		f.write(json.dumps(names, sort_keys=False, indent =2))

def ilvlPerItem(itemName):
    with open(trinketsDAJson) as f:
        ilvlList = list()
        data = json.load(f)
        for x in data:
            itemName = itemName.replace('_',' ').rstrip()
            n = re.search(r"\D*",x['actor']).group(0).replace('_',' ').rstrip()
            m = re.search(r'\d*',x['actor'].lstrip().split('_')[-1]).group(0)
            if itemName == n:
                ilvlList.append(m)
        uniqueList = make_unique(ilvlList)
    return uniqueList


trinketnames = getNames(trinketsDAJson)
trinketilvl = getIlvl(trinketsDAJson)

def buildTrinketJsonChart(injsonFile, outjsonFile, simType):
    '''
    injsonFile - The original CSV data converted to a raw unformatted JSON
    outjsonFile - The newly formatted JSON
    simType - Composite, Single Target, Dungeons
    '''
    #trinketnames = getNames(injsonFile) #Get all the trinket names from the inputted JSON file
    namelist = list()
    j = open(outjsonFile,'w') #Start writing our JSON file
    j.write('{\n') #JSON formatting
    with open(injsonFile,'r') as f: #Start reading the inputted JSON file.
        data = json.load(f)
        for x in data: #Easier to parse the originally converted JSON to organize the data
            m = re.search(r"\D*",x['actor'].rstrip()).group(0)
            namelist.append(m)
        uniqueList = make_unique(namelist)
        j.write('\t"data": {\n')
        ucntMax = len(uniqueList)
        ucnt = 0
        for u in uniqueList:
            ucnt+=1
            trinketilvl = ilvlPerItem(u)
            j.write('\t\t"' + u.replace('_',' ').rstrip() +'": {\n')
            maxCnt = len(trinketilvl)
            cnt = 0
            for y in trinketilvl:
                cnt+=1
                for x in data:
                    if x['profile'] == simType and x['actor'] == str(u+y):
                        if x['actor'] == 'Base':
                            j.write('\t\t\t"300": '+x['DPS']+'\n')
                        else:
                            if cnt < maxCnt:
                                j.write('\t\t\t"'+y+'": '+x['DPS']+',\n')
                            else:
                                j.write('\t\t\t"'+y+'": '+x['DPS']+'\n')
            if ucnt < ucntMax:
                j.write('\t\t},\n')
            else:
                j.write('\t\t}\n')
        j.write('\t},\n')
        j.write('\t"Data_type": "trinkets",\n\t"item_ids" : {\n')
        maxCnt = len(uniqueList)
        cnt = 0
        for u in uniqueList:
            cnt+=1
            u = u.replace(' ','_')
            if not u == 'Base':
                u = u[:-1]
            itemID = getItemId(u)
            if not str(itemID) == 'None':
                if cnt < maxCnt-1:
                    j.write('\t\t"'+u+'": '+str(itemID)+',\n')
                else:
                    j.write('\t\t"'+u+'": '+str(itemID)+'\n')
            else:
                if not u == 'Base':
                    print('Error: ' + u + ' Trinket was not included, likely due to a spelling error')
                    cnt+=1

        j.write('\t},\n')
        j.write('\t"simulated_steps": [\n')
        ilvls = getIlvl(injsonFile)
        ilvls = ilvls[:-1]
        cnt = 0
        maxCnt = len(ilvls)
        for i in ilvls:
            cnt+=1
            if cnt < maxCnt:
                j.write('\t\t'+str(i)+',\n')
            else:
                j.write('\t\t'+str(i)+'\n')
        j.write('\t],\n')
        DPSSort = list()
        for u in uniqueList:
            maxIlvl = ilvlPerItem(u)[0]
            for x in data:
                if x['profile'] == simType and x['actor'] == str(u+maxIlvl):
                    DPSSort.append(x['DPS'])
        sortedTrinkets = [x for _,x in sorted(zip(DPSSort, uniqueList),reverse=True)]
        ucnt = 0
        j.write('\t"sorted_data_keys": [\n')
        for s in sortedTrinkets:
            ucnt+=1
            if ucnt < ucntMax:
                j.write('\t\t"'+s+'",\n')
            else:
                j.write('\t\t"'+s+'"\n')
        j.write('\t]')
        #j.write('\n\t},')
        j.write('\n}')
    j.close()

def buildTraitJsonChart(injsonFile, outjsonFile, simType):
    '''
    injsonFile - The original CSV data converted to a raw unformatted JSON
    outjsonFile - The newly formatted JSON
    simType - Composite, Single Target, Dungeons
    '''

    namelist = list()
    j = open(outjsonFile,'w') #Start writing our JSON file
    j.write('{\n') #JSON formatting
    with open(injsonFile,'r') as f: #Start reading the inputted JSON file.
        data = json.load(f)
        for x in data: #Easier to parse the originally converted JSON to organize the data
            m = re.search(r"\D*",x['actor'].rstrip()).group(0)
            namelist.append(m)
        uniqueList = make_unique(namelist)
        #print(uniqueList)
        j.write('\t"data": {\n')
        ucntMax = len(uniqueList)
        ucnt = 0
        for u in uniqueList:
            ucnt+=1
            traitSteps = ['1','2','3'] #Should always be 1-3 unless they add some random 4th azerite gear slot
            if not u.replace('_',' ').rstrip() == 'Int': #Pull the int sims out
                j.write('\t\t"' + u.replace('_',' ').rstrip() +'": {\n')
            maxCnt = 3
            cnt = 0
            for y in traitSteps:
                cnt+=1
                for x in data:
                    if x['profile'] == simType:
                        if x['actor'] == str(u+y):
                            if cnt < maxCnt:
                                j.write('\t\t\t"'+y+'_stack": '+x['DPS']+',\n')
                            else:
                                j.write('\t\t\t"'+y+'_stack": '+x['DPS']+'\n')
            if ucnt < ucntMax:
                if not u.replace('_',' ').rstrip() == 'Int': #Have to check for int sims again
                    j.write('\t\t},\n')
            else:
                for x in data:
                    if x['profile'] == simType and x['actor'] == 'Base':
                        j.write('\t\t\t"1": '+x['DPS']+'\n')
                j.write('\t\t}\n')
        j.write('\t},\n')
        j.write('\t"Data_type": "traits",\n\t"spell_ids" : {\n')
        #Manually write in spell id's for traits
        j.write('\t\t"Archive of the Titans ":'+'"280708"'+',\n')
        j.write('\t\t"Azerite Globules ":'+'"279955"'+',\n')
        j.write('\t\t"Barrage Of Many Bombs ":'+'"280163"'+',\n')
        j.write('\t\t"Battlefield Focus ":'+'"280582"'+',\n')
        j.write('\t\t"Blightborne Infusion ":'+'"273823"'+',\n')
        j.write('\t\t"Blood Rite ":'+'"280409"'+',\n')
        j.write('\t\t"Blood Siphon ":'+'"264108"'+',\n')
        j.write('\t\t"Champion of Azeroth ":'+'"270583"'+',\n')
        j.write('\t\t"Chorus of Insanity ":'+'"278661"'+',\n')
        j.write('\t\t"Collective Will ":'+'"280837"'+',\n')
        j.write('\t\t"Combined Might ":'+'"280848"'+',\n')
        j.write('\t\t"Dagger in the Back Behind ":'+'"280285"'+',\n')
        j.write('\t\t"Dagger in the Back Front ":'+'"280285"'+',\n')
        j.write('\t\t"Death Throes ":'+'"278659"'+',\n')
        j.write('\t\t"Earthlink ":'+'"279927"'+',\n')
        j.write('\t\t"Elemental Whirl ":'+'"270667"'+',\n')
        j.write('\t\t"Filthy Transfusion ":'+'"273836"'+',\n')
        j.write('\t\t"Glory in Battle ":'+'"280852"'+',\n')
        j.write('\t\t"Gutripper ":'+'"266937"'+',\n')
        j.write('\t\t"Heed My Call ":'+'"271681"'+',\n')
        j.write('\t\t"Incite the Pack ":'+'"280410"'+',\n')
        j.write('\t\t"Laser Matrix ":'+'"280702"'+',\n')
        j.write('\t\t"Lifespeed":'+'"267665"'+',\n')
        j.write('\t\t"Meticulous Scheming ":'+'"273684"'+',\n')
        j.write('\t\t"On My Way ":'+'"267879"'+',\n')
        j.write('\t\t"Overwhelming Power ":'+'"266180"'+',\n')
        j.write('\t\t"Relational Normalization Gizmo ":'+'"280178"'+',\n')
        j.write('\t\t"Retaliatory Fury ":'+'"280785"'+',\n')
        j.write('\t\t"Rezans Fury ":'+'"281834"'+',\n')
        j.write('\t\t"Ricocheting Inflatable Pyrosaw ":'+'"280168"'+',\n')
        j.write('\t\t"Ruinous Bolt ":'+'"280206"'+',\n')
        j.write('\t\t"Searing Dialogue ":'+'"272788"'+',\n')
        j.write('\t\t"Secrets of the Deep ":'+'"273829"'+',\n')
        j.write('\t\t"Spiteful Apparitions ":'+'"277682"'+',\n')
        j.write('\t\t"Swirling Sands ":'+'"280433"'+',\n')
        j.write('\t\t"Sylvanas Resolve ":'+'"280810"'+',\n')
        j.write('\t\t"Synaptic Spark Capacitor ":'+'"280174"'+',\n')
        j.write('\t\t"Thought Harvester ":'+'"273320"'+',\n')
        j.write('\t\t"Thunderous Blast ":'+'"280384"'+',\n')
        j.write('\t\t"Tidal Surge ":'+'"280404"'+',\n')
        j.write('\t\t"Tradewinds ":'+'"281843"'+',\n')
        j.write('\t\t"Unstable Catalyst ":'+'"281516"'+',\n')
        j.write('\t\t"Unstable Flames ":'+'"279902"'+',\n')
        j.write('\t\t"Whispers of the Damned ":'+'"275726"'+'\n')
        j.write('\t},\n')
        #end manual
        j.write('\t"simulated_steps": [\n')
        #write the 3 levels of traits
        j.write('\t\t"1_Stack",\n')
        j.write('\t\t"2_Stack",\n')
        j.write('\t\t"3_Stack"\n')
        j.write('\t],\n')
        DPSSort = list()
        for u in uniqueList:
            for x in data:
                if x['profile'] == simType and x['actor'] == str(u+'1'):
                    DPSSort.append(x['DPS'])
        sortedTraits = [x for _,x in sorted(zip(DPSSort, uniqueList),reverse=True)]
        ucnt = 0
        j.write('\t"sorted_data_keys": [\n')
        sortedTraits = sortedTraits[:-1] #Remove Int_ since it will always be the last option.
        for s in sortedTraits:
            ucnt+=1
            if ucnt < ucntMax:
                j.write('\t\t"'+s.replace('_',' ')+'",\n')
            else:
                j.write('\t\t"'+s.replace('_',' ')+'"\n')
        j.write('\t\t"Base"\n')
        j.write('\t]')
        #j.write('\n\t},')
        j.write('\n}')
    j.close()

os.chdir("json_Charts/")

buildTrinketJsonChart(trinketsDAJson, "trinkets_DA_C.json", 'composite')
buildTrinketJsonChart(trinketsDAJson, "trinkets_DA_ST.json", 'single_target')
buildTrinketJsonChart(trinketsLotVJson, "trinkets_LotV_C.json", 'composite')
buildTrinketJsonChart(trinketsLotVJson, "trinkets_LotV_ST.json", 'single_target')
buildTraitJsonChart(traitsDAJson, "traits_DA_C.json", 'composite')
buildTraitJsonChart(traitsDAJson, "traits_DA_ST.json", 'single_target')
buildTraitJsonChart(traitsLotVJson, "traits_LotV_C.json", 'composite')
buildTraitJsonChart(traitsLotVJson, "traits_LotV_ST.json", 'single_target')

os.chdir('..')

os.remove(trinketsDAJson)
os.remove(trinketsLotVJson)
os.remove(traitsDAJson)
os.remove(traitsLotVJson)



endtime = time.time()
totaltime = endtime-starttime
print("Sucessfully converted charts to JSON format in %d seconds" % (totaltime))
