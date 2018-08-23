import csv
import json
import re

#Define all file paths
#Trinkets
trinketsDA = 'trinkets/Results_DA.csv'
trinketsLotV = 'trinkets/Results_LotV.csv'

#Triats
traitsDA = 'azerite-traits/Results_DA.csv'
traitsLotV = 'azerite-traits/Results_LotV.csv'

#JSON Files
#Trinkets
trinketsDAJson = 'trinkets/Results_DA.json'
trinketsLotVJson = 'trinkets/Results_LotV.json'
#Traits
traitsDAJson = 'azerite-traits/Results_DA.json'
traitsLotVJson = 'azerite-traits/Results_LotV.json'

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
    with open('trinkets/trinkets_dungeons_DA.simc','r') as f:
        lines = f.readlines()
        for line in lines:
            try:
                if re.search(r'(trinket1=)\D*',line)[0].replace('trinket1=','').replace(',id=','') == itemname:
                    itemID = re.search(r'(id=)\d*',line.strip('\n'))[0].strip('id=')
                    return itemID
            except:
                continue
    with open('trinkets/trinkets_other_DA.simc','r') as f:
        lines = f.readlines()
        for line in lines:
            try:
                if re.search(r'(trinket1=)\D*',line)[0].replace('trinket1=','').replace(',id=','') == itemname:
                    itemID = re.search(r'(id=)\d*',line)[0].strip('id=')
                    return itemID
            except:
                continue
    with open('trinkets/trinkets_raid_DA.simc','r') as f:
        lines = f.readlines()
        for line in lines:
            try:
                if re.search(r'(trinket1=)\D*',line)[0].replace('trinket1=','').replace(',id=','') == itemname:
                    itemID = re.search(r'(id=)\d*',line)[0].strip('id=')
                    return itemID
            except TypeError:
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
			m = re.search(r"\D*",x['actor'])[0].replace('_',' ').rstrip()
			nameList.append(m)
		uniqueList = make_unique(nameList)
	return uniqueList

def getIlvl(jsonFile):
    with open(jsonFile,'r') as f:
        nameList = list()
        data = json.load(f)
        for x in data:
            m = re.search(r"\d*",x['actor'].lstrip().split('_')[-1])[0]
            nameList.append(m)
        uniqueList = make_unique(nameList)
        #Clear out empty spaces
        #for x in uniqueList:
        #    if x == "":
        #        uniqueList.remove(x)
    return uniqueList

def addNamesToJson(jsonFile):
	names = getNames(jsonFile)
	with open(jsonFile, 'r+') as f:
		data = json.load(f)
		data.append(names)
		f.write(json.dumps(names, sort_keys=False, indent =2))


trinketnames = getNames(trinketsDAJson)
trinketilvl = getIlvl(trinketsDAJson)

def buildJsonChart(injsonFile, outjsonFile):
    trinketnames = getNames(injsonFile)
    trinketilvl = getIlvl(injsonFile)
    namelist = list()
    j = open(outjsonFile,'w')
    j.write('[\n')
    with open(injsonFile,'r') as f:
        data = json.load(f)
        for x in data:
            m = re.search(r"\D*",x['actor'].rstrip())[0]
            namelist.append(m)
        uniqueList = make_unique(namelist)
        j.write('\t"data": {\n')
        for u in uniqueList:
            j.write('\t\t"' + u.replace('_',' ').rstrip() +'": {\n')
            for y in trinketilvl:
                for x in data:
                    if x['profile'] == 'composite' and x['actor'] == str(u+y):
                        if x['actor'] == 'Base':
                            j.write('\t\t\t"300": '+x['DPS']+'\n')
                        else:
                            j.write('\t\t\t"'+y+'": '+x['DPS']+'\n')
            j.write('\t\t},\n')
        j.write('\t},\n')
        j.write('\t"Data_type": "trinkets",\n\t"item_ids" : {\n')
        for u in uniqueList:
            u = u.replace(' ','_')
            if not u == 'Base':
                u = u[:-1]
            itemID = getItemId(u)
            if not str(itemID) == 'None':
                j.write('\t\t"'+u+'": '+str(itemID)+',\n')
            else:
                print(u)
        
        j.write('\t},\n]')
    j.close()

buildJsonChart(trinketsDAJson, "testing.json")

#addNamesToJson(trinketsDAJson)
itemid = getItemId('Tzanes_Barkspines')
print(itemid)