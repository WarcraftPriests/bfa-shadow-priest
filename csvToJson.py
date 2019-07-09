import csv
import json
import re
import time
import os
import datetime

starttime = time.time()

#Define all file paths
#Trinkets
trinketsSC = os.path.os.path.abspath(os.path.join(os.getcwd(), 'trinkets/Results_SC.csv'))
trinketsAS = os.path.os.path.abspath(os.path.join(os.getcwd(), 'trinkets/Results_AS.csv'))
trinketsSCD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'trinkets/Results_Dungeons_SC.csv'))
trinketsASD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'trinkets/Results_Dungeons_AS.csv'))

#Triats
traitsSC = os.path.os.path.abspath(os.path.join(os.getcwd(), 'azerite-traits/Results_SC.csv'))
traitsAS = os.path.os.path.abspath(os.path.join(os.getcwd(), 'azerite-traits/Results_AS.csv'))
traitsSCD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'azerite-traits/Results_Dungeons_SC.csv'))
traitsASD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'azerite-traits/Results_Dungeons_AS.csv'))

#Essences
essencesSC = os.path.os.path.abspath(os.path.join(os.getcwd(), 'essences/Results_SC.csv'))
essencesAS = os.path.os.path.abspath(os.path.join(os.getcwd(), 'essences/Results_AS.csv'))
essencesSCD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'essences/Results_Dungeons_SC.csv'))
essencesASD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'essences/Results_Dungeons_AS.csv'))

#Talents
talents = os.path.os.path.abspath(os.path.join(os.getcwd(), 'talents/Results.csv'))
talentsD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'talents/results_Dungeons.csv'))

#Racials
racialsAS = os.path.os.path.abspath(os.path.join(os.getcwd(), 'racials/Results_AS.csv'))
racialsASD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'racials/Results_Dungeons_AS.csv'))
racialsSC = os.path.os.path.abspath(os.path.join(os.getcwd(), 'racials/Results_SC.csv'))
racialsSCD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'racials/Results_Dungeons_SC.csv'))

#Enchants
enchantsAS = os.path.os.path.abspath(os.path.join(os.getcwd(), 'enchants/Results_AS.csv'))
enchantsASD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'enchants/Results_Dungeons_AS.csv'))
enchantsSC = os.path.os.path.abspath(os.path.join(os.getcwd(), 'enchants/Results_SC.csv'))
enchantsSCD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'enchants/Results_Dungeons_SC.csv'))

#Consumables
consumablesAS = os.path.os.path.abspath(os.path.join(os.getcwd(), 'consumables/Results_AS.csv'))
consumablesASD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'consumables/Results_Dungeons_AS.csv'))
consumablesSC = os.path.os.path.abspath(os.path.join(os.getcwd(), 'consumables/Results_SC.csv'))
consumablesSCD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'consumables/Results_Dungeons_SC.csv'))

#JSON Files
#Trinkets
trinketsSCJson = os.path.os.path.abspath(os.path.join(os.getcwd(), 'trinkets/Results_SC.json'))
trinketsASJson = os.path.os.path.abspath(os.path.join(os.getcwd(), 'trinkets/Results_AS.json'))
trinketsSCJsonD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'trinkets/Results_SC_D.json'))
trinketsASJsonD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'trinkets/Results_AS_D.json'))
#Traits
traitsSCJson = os.path.os.path.abspath(os.path.join(os.getcwd(), 'azerite-traits/Results_SC.json'))
traitsASJson = os.path.os.path.abspath(os.path.join(os.getcwd(), 'azerite-traits/Results_AS.json'))
traitsSCJsonD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'azerite-traits/Results_SC_D.json'))
traitsASJsonD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'azerite-traits/Results_AS_D.json'))
#Essences
essencesSCJson = os.path.os.path.abspath(os.path.join(os.getcwd(), 'essences/Results_SC.json'))
essencesASJson = os.path.os.path.abspath(os.path.join(os.getcwd(), 'essences/Results_AS.json'))
essencesSCJsonD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'essences/Results_SC_D.json'))
essencesASJsonD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'essences/Results_AS_D.json'))
#Talents
talentsJson = os.path.os.path.abspath(os.path.join(os.getcwd(), 'talents/Results.json'))
talentsJsonD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'talents/Results_D.json'))

#Racials
racialsASJson = os.path.os.path.abspath(os.path.join(os.getcwd(), 'racials/Results_AS.json'))
racialsASJsonD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'racials/Racials_AS_D.json'))
racialsSCJson = os.path.os.path.abspath(os.path.join(os.getcwd(), 'racials/Results_SC.json'))
racialsSCJsonD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'racials/Racials_SC_D.json'))

#Enchants
enchantsASJson = os.path.os.path.abspath(os.path.join(os.getcwd(), 'enchants/Results_AS.json'))
enchantsASJsonD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'enchants/enchants_AS_D.json'))
enchantsSCJson = os.path.os.path.abspath(os.path.join(os.getcwd(), 'enchants/Results_SC.json'))
enchantsSCJsonD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'enchants/enchants_SC_D.json'))

#Consumables
consumablesASJson = os.path.os.path.abspath(os.path.join(os.getcwd(), 'consumables/Results_AS.json'))
consumablesASJsonD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'consumables/consumables_AS_D.json'))
consumablesSCJson = os.path.os.path.abspath(os.path.join(os.getcwd(), 'consumables/Results_SC.json'))
consumablesSCJsonD = os.path.os.path.abspath(os.path.join(os.getcwd(), 'consumables/consumables_SC_D.json'))

# SimC files
trinketsDungeonsSC = os.path.os.path.abspath(os.path.join(os.getcwd(), 'trinkets/trinkets_dungeons_SC.simc'))
trinketsOtherSC = os.path.os.path.abspath(os.path.join(os.getcwd(), 'trinkets/trinkets_other_SC.simc'))
trinketsRaidSC = os.path.os.path.abspath(os.path.join(os.getcwd(), 'trinkets/trinkets_raid_SC.simc'))

#CSV Field names
fieldnames = ('profile', 'actor', 'DPS', 'increase')

now = datetime.datetime.now()
now = str(now.year) + "/" + str(now.month) + "/" + str(now.day)


# Trait List (hack fix for the moment)
traitList = [
'Ancients_Bulwark_',
'Apothecarys_Concoctions_',
'Arcane_Heart_',
'Barrage_Of_Many_Bombs_',
'Battlefield_Focus_',
'Blightborne_Infusion_',
'Blood_Rite_',
'Bonded_Souls_',
'Champion_of_Azeroth_',
'Chorus_of_Insanity_',
'Clockwork_Heart_',
'Collective_Will_',
'Combined_Might_',
'Dagger_in_the_Back_Behind_',
'Dagger_in_the_Back_Front_',
'Death_Throes_',
'Fight_or_Flight_',
'Filthy_Transfusion_',
'Glory_in_Battle_',
'Incite_the_Pack_',
'Loyal_to_the_End_',
'Meticulous_Scheming_',
'Relational_Normalization_Gizmo_',
'Retaliatory_Fury_',
'Rezans_Fury_',
'Ricocheting_Inflatable_Pyrosaw_',
'Ruinous_Bolt_',
'Searing_Dialogue_',
'Secrets_of_the_Deep_',
'Seductive_Power_',
'Shadow_of_Elune_',
'Spiteful_Apparitions_',
'Swirling_Sands_',
'Sylvanas_Resolve_',
'Synaptic_Spark_Capacitor_',
'Thought_Harvester_',
'Thunderous_Blast_',
'Tidal_Surge_',
'Tradewinds_',
'Treacherous_Covenant_',
'Undulating_Tides_',
'Unstable_Catalyst_',
'Whispers_of_the_Damned_',

#Secondary Traits
'Azerite_Globules_',
'Blood_Siphon_',
'Earthlink_',
'Elemental_Whirl_',
'Gutripper_',
'Heed_My_Call_',
'On_My_Way_',
'Overwhelming_Power_',
'Unstable_Flames_']

essences = {
    #Majors
    'Blood of the Enemy' : 'Blood of the Enemy',
    'Guardian of Azeroth' : 'Condensed Life-Force',
    'Focused Azerite Beam' : 'Essence of the Focusing Iris',
    'Purifying Blast' : 'Purification Protocol',
    'The Unbound Force' : 'The Unbound Force',
    'Memory of Lucid Dreams' : 'Memory of Lucid Dreams',
    'Vision of Perfection' : 'Vision of Perfection',
    'Conflict' : 'Conflict and Strife',
    'Concentrated Flame' : 'The Crucible of Flame',
    'Rippled in Space' : 'Rippled in Space',
    'Worldvein Resonance' : 'Worldvein Resonance',


    #Minors
    'Blood-Soaked' : 'Blood of the Enemy',
    'Condensed Life-Force' : 'Condensed Life-Force',
    'Focused Energy' : 'Essence of the Focusing Iris',
    'Purification Protocol' : 'Purification Protocol',
    'Reckless Force' : 'The Unbound Force',
    'Lucid Dreams' : 'Memory of Lucid Dreams',
    'Strive for Perfection' : 'Vision of Perfection',
    'Strife' : 'Conflict and Strife',
    'Lifeblood' : 'Worldvein Resonance',
    'Ancient Flame' : 'The Crucible of Flame',
    'Reality Shift' : 'Rippled in Space'
}



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


parseCSV(trinketsSC,trinketsSCJson)
parseCSV(trinketsAS,trinketsASJson)
parseCSV(trinketsSCD,trinketsSCJsonD)
parseCSV(trinketsASD,trinketsASJsonD)

parseCSV(traitsSC,traitsSCJson)
parseCSV(traitsAS,traitsASJson)
parseCSV(traitsSCD,traitsSCJsonD)
parseCSV(traitsASD,traitsASJsonD)

parseCSV(essencesAS,essencesASJson)
parseCSV(essencesSC,essencesSCJson)
parseCSV(essencesASD,essencesASJsonD)
parseCSV(essencesSCD,essencesSCJsonD)

parseCSV(talents, talentsJson)
parseCSV(talentsD, talentsJsonD)

parseCSV(racialsAS, racialsASJson)
parseCSV(racialsASD, racialsASJsonD)
parseCSV(racialsSC, racialsSCJson)
parseCSV(racialsSCD, racialsSCJsonD)

parseCSV(enchantsAS, enchantsASJson)
parseCSV(enchantsASD, enchantsASJsonD)
parseCSV(enchantsSC, enchantsSCJson)
parseCSV(enchantsSCD, enchantsSCJsonD)

parseCSV(consumablesAS, consumablesASJson)
parseCSV(consumablesASD, consumablesASJsonD)
parseCSV(consumablesSC, consumablesSCJson)
parseCSV(consumablesSCD, consumablesSCJsonD)

def getItemId(itemname):
    itemname = itemname.lower().rstrip()
    with open(trinketsDungeonsSC, 'r') as f:
        lines = f.readlines()
        for line in lines:
            try:
                if re.search(r'(trinket1=)\D*',line).group(0).replace('trinket1=','').replace(',id=','').lower() == itemname:
                    itemID = re.search(r'(id=)\d*',line.strip('\n')).group(0).strip('id=')
                    return itemID
            except:
                continue
    with open(trinketsOtherSC, 'r') as f:
        lines = f.readlines()
        for line in lines:
            try:
                if re.search(r'(trinket1=)\D*',line).group(0).replace('trinket1=','').replace(',id=','').lower() == itemname:
                    itemID = re.search(r'(id=)\d*',line).group(0).strip('id=')
                    return itemID
            except:
                continue
    with open(trinketsRaidSC, 'r') as f:
        lines = f.readlines()
        for line in lines:
            try:
                if re.search(r'(trinket1=)\D*',line).group(0).replace('trinket1=','').replace(',id=','').lower() == itemname:
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
        uniqueList.sort(reverse=True)
        print(uniqueList)
    return uniqueList

def addNamesToJson(jsonFile):
    names = getNames(jsonFile)
    with open(jsonFile, 'r+') as f:
        data = json.load(f)
        data.append(names)
        f.write(json.dumps(names, sort_keys=False, indent =2))

def ilvlPerItem(itemName):
    with open(trinketsSCJson) as f:
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


trinketnames = getNames(trinketsSCJson)
trinketilvl = getIlvl(trinketsSCJson)

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
                    print('Error: ' + u + ' Trinket was not included in the item ID list.')

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
            try:
                maxIlvl = ilvlPerItem(u)[0]
            except:
                print('Error: ' + u + ' Trinket was not included in the item ID list.')
            for x in data:
                if x['profile'] == simType and x['actor'] == str(u+maxIlvl):
                    DPSSort.append(x['DPS'])
        sortedTrinkets = [x for _,x in sorted(zip(DPSSort, uniqueList),reverse=True)]
        sortedTrinkets = sortedTrinkets[:-1] #Remove Base since it will always be the last option.
        ucnt = 0
        ucntMax = len(sortedTrinkets)
        j.write('\t"sorted_data_keys": [\n')
        for s in sortedTrinkets:
            ucnt+=1
            if not s == 'Base':
                if ucnt < ucntMax:
                    j.write('\t\t"'+s.replace('_',' ').strip()+'",\n')
                else:
                    j.write('\t\t"'+s.replace('_',' ').strip()+'"\n')
        j.write('\t],\n')
        #j.write('\n\t},')
        j.write('\t"LastUpdated": [\n')
        j.write('\t\t"' + now + '"\n')
        j.write('\t]')
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
        if "Base" in uniqueList: uniqueList.remove("Base")
        if "Int_" in uniqueList: uniqueList.remove("Int_")
        j.write('\t"data": {\n')
        ucntMax = len(uniqueList)
        #print(ucntMax)
        ucnt = 0
        for u in uniqueList:
            ucnt+=1
            traitSteps = ['1','2','3'] #Should always be 1-3 unless they add some random 4th azerite gear slot
            if not u.replace('_',' ').rstrip() == 'Int' or u == 'Base': #Pull the int sims out
                j.write('\t\t"' + u.replace('_',' ').rstrip() +'": {\n')
            maxCnt = 3
            cnt = 0
            for y in traitSteps:
                cnt+=1
                for x in data:
                    if x['profile'] == simType:
                        if x['actor'] == str(u+y) and 'base' not in x['actor'].lower():
                            if x['actor']== ("Champion_of_Azeroth_" + y):
                                j.write('\t\t\t"1_stack": '+x['DPS']+',\n')
                                j.write('\t\t\t"2_stack": 0,\n')
                                j.write('\t\t\t"3_stack": 0\n') #Have to add empty stacks here because highcharts is dumb.
                            elif 'combo' in x['actor']:
                                j.write('\t\t\t"1_stack": 0,\n')
                                j.write('\t\t\t"2_stack": ' + x['DPS']+',\n')
                                j.write('\t\t\t"3_stack": 0' + '\n')
                            else:
                                if cnt < maxCnt:
                                    j.write('\t\t\t"'+y+'_stack": '+x['DPS']+',\n')
                                else:
                                    j.write('\t\t\t"'+y+'_stack": '+x['DPS']+'\n')
            if ucnt < ucntMax:
                if not u.replace('_',' ').rstrip() == 'Int': #Have to check for int sims again
                    j.write('\t\t},\n')
            if ucnt == ucntMax:
                j.write('\t\t},')
                for x in data:
                    if x['profile'] == simType and x['actor'] == 'Base':
                        j.write('\n\t\t"Base": {\n')
                        j.write('\t\t\t"1_stack": '+x['DPS']+',\n')
                        j.write('\t\t\t"2_stack": 0,\n')
                        j.write('\t\t\t"3_stack": 0\n') #Have to add empty stacks here because highcharts is dumb.
                j.write('\t\t}\n')
        j.write('\t},\n')
        j.write('\t"Data_type": "traits",\n\t"spell_ids" : {\n')
        #Manually write in spell id's for traits
        j.write('\t\t"Ancients Bulwark ":'+'"287631"'+',\n')
        j.write('\t\t"Apothecarys Concoctions ":'+'"287604"'+',\n')
        j.write('\t\t"Arcane Heart ":'+'"303006"'+',\n')
        j.write('\t\t"Archive of the Titans ":'+'"280708"'+',\n')
        j.write('\t\t"Azerite Empowered ":'+'"263978"'+',\n')
        j.write('\t\t"Azerite Globules ":'+'"279955"'+',\n')
        j.write('\t\t"Barrage Of Many Bombs ":'+'"280163"'+',\n')
        j.write('\t\t"Battlefield Focus ":'+'"280582"'+',\n')
        j.write('\t\t"Blightborne Infusion ":'+'"273823"'+',\n')
        j.write('\t\t"Blood Rite ":'+'"280409"'+',\n')
        j.write('\t\t"Blood Siphon ":'+'"264108"'+',\n')
        j.write('\t\t"Bonded Souls ":'+'"288841"'+',\n')
        j.write('\t\t"Champion of Azeroth ":'+'"270583"'+',\n')
        j.write('\t\t"Chorus of Insanity ":'+'"278661"'+',\n')
        j.write('\t\t"Clockwork Heart ":'+'"300210"'+',\n')
        j.write('\t\t"Collective Will ":'+'"280837"'+',\n')
        j.write('\t\t"Combined Might ":'+'"280848"'+',\n')
        j.write('\t\t"Dagger in the Back Behind ":'+'"280285"'+',\n')
        j.write('\t\t"Dagger in the Back Front ":'+'"280285"'+',\n')
        j.write('\t\t"Death Throes ":'+'"278659"'+',\n')
        j.write('\t\t"Earthlink ":'+'"279927"'+',\n')
        j.write('\t\t"Elemental Whirl ":'+'"270667"'+',\n')
        j.write('\t\t"Endless Hunger ":'+'"287662"'+',\n')
        j.write('\t\t"Fight or Flight ":'+'"287818"'+',\n')
        j.write('\t\t"Filthy Transfusion ":'+'"273836"'+',\n')
        j.write('\t\t"Glory in Battle ":'+'"280852"'+',\n')
        j.write('\t\t"Gutripper ":'+'"266937"'+',\n')
        j.write('\t\t"Heed My Call ":'+'"271681"'+',\n')
        j.write('\t\t"Incite the Pack ":'+'"280410"'+',\n')
        j.write('\t\t"Laser Matrix ":'+'"280702"'+',\n')
        j.write('\t\t"Loyal to the End ":'+'"303007"'+',\n')
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
        j.write('\t\t"Shadow of Elune ": ' + '"287471" ' + ',\n')
        j.write('\t\t"Spiteful Apparitions ":'+'"277682"'+',\n')
        j.write('\t\t"Swirling Sands ":'+'"280433"'+',\n')
        j.write('\t\t"Sylvanas Resolve ":'+'"280810"'+',\n')
        j.write('\t\t"Synaptic Spark Capacitor ":'+'"280174"'+',\n')
        j.write('\t\t"Thought Harvester ":'+'"273320"'+',\n')
        j.write('\t\t"Thunderous Blast ":'+'"280384"'+',\n')
        j.write('\t\t"Tidal Surge ":'+'"280404"'+',\n')
        j.write('\t\t"Tradewinds ":'+'"281843"'+',\n')
        j.write('\t\t"Treacherous Covenant ":'+'"288989"'+',\n')
        j.write('\t\t"Undulating Tides ":'+'"303008"'+',\n')
        j.write('\t\t"Unstable Catalyst ":'+'"281516"'+',\n')
        j.write('\t\t"Unstable Flames ":'+'"279902"'+',\n')
        j.write('\t\t"Whispers of the Damned ":'+'"275726"'+'\n')
        j.write('\t},\n')
        #end manual
        j.write('\t"simulated_steps": [\n')
        #write the 3 levels of traits
        j.write('\t\t"1_stack",\n')
        j.write('\t\t"2_stack",\n')
        j.write('\t\t"3_stack"\n')
        j.write('\t],\n')
        DPSSort = dict()
        for u in traitList:
            for x in data:
                if x['profile'] == simType and x['actor'] == str(u+'1'):
                    u = u.replace('_'," ").rstrip()
                    DPSSort.update({u : x['DPS']})
        #if "Int_" in uniqueList: uniqueList.remove("Int_")
        import operator
        sorted_x = sorted(DPSSort.items(), key=operator.itemgetter(1), reverse=True)


        j.write('\t"sorted_data_keys": [\n')
        cnt=0
        ucntMax = len(sorted_x)
        for key in sorted_x:
            cnt+=1
            if 'Int' not in key[0]:
                if cnt < ucntMax:
                    j.write('\t\t "' + key[0] + '",\n')
                else:
                    j.write('\t\t "' + key[0] + '"\n')
        j.write('\t]')
        #j.write('\n\t},')
        j.write('\n}')
    j.close()


def buildTraitJsonComboChart(injsonFile, outjsonFile, simType):
    namelist = list()
    j = open(outjsonFile,'w') #Start writing our JSON file
    j.write('{\n') #JSON formatting
    with open(injsonFile,'r') as f: #Start reading the inputted JSON file.
        data = json.load(f)
        for x in data: #Easier to parse the originally converted JSON to organize the data
            m = re.search(r"\w*",x['actor'].rstrip()).group(0)
            if "combo" in m:
                namelist.append(m)
        uniqueList = make_unique(namelist)
        if "Base" in uniqueList: uniqueList.remove("Base")
        j.write('\t"data": {\n')
        ucntMax = len(uniqueList)
        #print(ucntMax)
        ucnt = 0
        for u in uniqueList:
            ucnt+=1
            traitSteps = ['1']
            if not u.replace('_',' ').rstrip() == 'Int' or u == 'Base': #Pull the int sims out
                j.write('\t\t"' + u.replace('_',' ').replace('combo 6', ' ').replace('combo 5', ' ').replace('combo 4', ' ').replace('combo 3', ' ').replace('combo 2', ' ').rstrip() +'": {\n')
            maxCnt = 3
            cnt = 0
            for y in traitSteps:
                cnt+=1
                for x in data:
                    if x['profile'] == simType:
                        if x['actor'] == str(u):
                            if cnt < maxCnt:
                                j.write('\t\t\t"'+'1_stack": '+x['DPS']+'\n')
                            else:
                                j.write('\t\t\t"'+'1_stack": '+x['DPS']+'\n')
            if ucnt < ucntMax:
                if not u.replace('_',' ').rstrip() == 'Int': #Have to check for int sims again
                    j.write('\t\t},\n')
            else:
                j.write('\t\t},')
                for x in data:
                    if x['profile'] == simType and x['actor'] == 'Base':
                        j.write('\n\t\t"Base": {\n')
                        j.write('\t\t\t"1_stack": '+x['DPS']+',\n')
                j.write('\t\t}\n')
        j.write('\t},\n')
        DPSSort = list()
        for u in uniqueList:
            for x in data:
                if x['profile'] == simType and x['actor'] == str(u):
                    DPSSort.append(x['DPS'])
        #if "Int_" in uniqueList: uniqueList.remove("Int_")
        sortedTraits = [x for _,x in sorted(zip(DPSSort, uniqueList),reverse=True)]
        j.write('\t"sorted_data_keys": [\n')
        ucntMax = len(sortedTraits)
        ucnt = 0
        for s in sortedTraits:
            ucnt+=1
            if not s == 'Base':
                s = s.replace('_',' ')
                s = s.replace(" combo 6", ' ')
                s = s.replace(" combo 5", ' ')
                s = s.replace(" combo 4", ' ')
                s = s.replace(" combo 3", ' ')
                s = s.replace(" combo 2", ' ')
                s = s.rstrip()
                if ucnt < ucntMax:
                    j.write('\t\t"'+s+'",\n')
                else:
                    j.write('\t\t"'+s+'"\n')
        j.write('\t]')
        #j.write('\n\t},')
        j.write('\n}')
    j.close()

def buildEssenceJsonChart(injsonFile, outjsonFile, simType):
    namelist = list()
    j = open(outjsonFile,'w') #Start writing our JSON file
    j.write('{\n') #JSON formatting
    with open(injsonFile,'r') as f: #Start reading the inputted JSON file.
        data = json.load(f)
        for x in data: #Easier to parse the originally converted JSON to organize the data
            m = re.search(r"\D*",x['actor'].rstrip()).group(0)
            namelist.append(m)
        uniqueList = make_unique(namelist)
        if "Base" in uniqueList: uniqueList.remove("Base")
        if "Blood_of_the_Enemy_" in uniqueList: uniqueList.remove("Blood_of_the_Enemy_")
        if "Lifeblood_" in uniqueList: uniqueList.remove("Lifeblood_")
        if "Worldvein_Resonance_" in uniqueList: uniqueList.remove("Worldvein_Resonance_")
        j.write('\t"data": {\n')
        ucntMax = len(uniqueList)
        ucnt = 0
        for u in uniqueList:
            j.write('\t\t"' + u.replace('_',' ').rstrip() +'": {\n')
            ucnt+=1
            essenceSteps = ['3', '2','1']
            maxCnt = 3
            cnt = 0
            for y in essenceSteps:
                cnt+=1
                for x in data:
                    if x['profile'] == simType:
                        if x['actor'] == str(u) + y:
                            if cnt < maxCnt:
                                j.write('\t\t\t"'+'rank_'+ y + '": '+x['DPS']+',\n')
                            else:
                                j.write('\t\t\t"'+'rank_1": '+x['DPS']+'\n')
            if ucnt < ucntMax:
                if not u.replace('_',' ').rstrip() == 'Int': #Have to check for int sims again
                    j.write('\t\t},\n')
            else:
                j.write('\t\t},')

                for x in data:
                    if x['profile'] == simType and x['actor'] == 'Base':
                        j.write('\n\t\t"Base": {\n')
                        j.write('\t\t\t"rank_1": '+x['DPS']+'\n')
                j.write('\t\t},\n')
        # Special Handling for Blood of the Enemy
        essenceSteps = ['3', '2','1']
        maxCnt = 3
        boteList = list()
        for x in data:
            if 'Blood_of_the_Enemy_' in x['actor']:
                temp = x['actor'].replace('_Uptime','')
                temp = temp[:-2]
                boteList.append(temp)
        boteList = make_unique(boteList)
        ucnt = 0
        ucntMax = len(boteList)
        for b in boteList:
            ucnt+=1
            cnt = 0
            j.write('\t\t"' + b.replace("_"," ") +'": {\n')
            for e in essenceSteps:
                cnt+=1
                for x in data:
                    if x['profile'] == simType:
                        if x['actor'].replace('_Uptime','') == b + '_' + e:
                               if cnt < maxCnt:
                                    j.write('\t\t\t"' + 'rank_' + e + '": '+ x['DPS']+',\n')
                               else:
                                    j.write('\t\t\t"'+'rank_1": '+x['DPS']+'\n')
            j.write('\t\t},\n')
        #Special Handling for WorldVein
        worldVeinList = list()
        for x in data:
            if "Worldvein" in x['actor']:
                temp = x['actor'].replace('Allies','')
                temp = temp[:-3]
                worldVeinList.append(temp)
        worldVeinList = make_unique(worldVeinList)
        allySteps = ['4','3','2','1']
        ucnt=0
        ucntMax = len(worldVeinList)
        for l in worldVeinList:
            ucnt+=1
            cnt = 0
            j.write('\t\t"' + l.replace('_',' ') + ' Allies' + '":{\n')
            for e in essenceSteps:
                cnt+=1
                for x in data:
                    if x['profile'] == simType:
                        if x['actor'] == l + '_Allies_' + e:
                            if cnt < maxCnt:
                                j.write('\t\t\t"' + 'rank_' + e + '": '+ x['DPS']+',\n')
                            else:
                                 j.write('\t\t\t"'+'rank_1": '+x['DPS']+'\n')
            j.write('\t\t},\n')

        #Special Handling for Lifeblood
        lifeBloodList = list()
        for x in data:
            if "Lifeblood" in x['actor']:
                temp = x['actor'].replace('Allies','')
                temp = temp[:-3]
                lifeBloodList.append(temp)
        lifeBloodList = make_unique(lifeBloodList)
        allySteps = ['4','3','2','1']
        ucnt=0
        ucntMax = len(lifeBloodList)
        for l in lifeBloodList:
            ucnt+=1
            cnt = 0
            j.write('\t\t"' + l.replace('_',' ') + ' Allies' + '":{\n')
            for e in essenceSteps:
                cnt+=1
                for x in data:
                    if x['profile'] == simType:
                        if x['actor'] == l + '_Allies_' + e:
                            if cnt < maxCnt:
                                j.write('\t\t\t"' + 'rank_' + e + '": '+ x['DPS']+',\n')
                            else:
                                 j.write('\t\t\t"'+'rank_1": '+x['DPS']+'\n')
            if ucnt < ucntMax:
                j.write('\t\t},\n')
            else:
                j.write('\t\t}\n')
        j.write('\t},\n')
        j.write('\t"spell_ids" : {\n')
        #Majors
        j.write('\t\t"Focused Azerite Beam" : 295258,\n')
        j.write('\t\t"Guardian of Azeroth" : 295840,\n')
        j.write('\t\t"Purifying Blast" : 295337,\n')
        j.write('\t\t"The Unbound Force" : 298452,\n')
        j.write('\t\t"Memory of Lucid Dreams" : 298357,\n')
        j.write('\t\t"Vision of Perfection" : 296325,\n')
        j.write('\t\t"Conflict" : 303823,\n')
        j.write('\t\t"Concentrated Flame" : 295373,\n')
        j.write('\t\t"Ripple in Space" : 302731,\n')

        #Special Majors
        j.write('\t\t"Blood of the Enemy 100" : 297108,\n')
        j.write('\t\t"Blood of the Enemy 75" : 297108,\n')
        j.write('\t\t"Blood of the Enemy 50" : 297108,\n')
        j.write('\t\t"Worldvein Resonance 4 Allies" : 295186,\n')
        j.write('\t\t"Worldvein Resonance 3 Allies" : 295186,\n')
        j.write('\t\t"Worldvein Resonance 2 Allies" : 295186,\n')
        j.write('\t\t"Worldvein Resonance 1 Allies" : 295186,\n')

        #Minors
        j.write('\t\t"Blood-Soaked" : 297147,\n')
        j.write('\t\t"Condensed Life-Force" : 295834,\n')
        j.write('\t\t"Focused Energy" : 295246,\n')
        j.write('\t\t"Purification Protocol" : 295293,\n')
        j.write('\t\t"Reckless Force" : 298452,\n')
        j.write('\t\t"Lucid Dreams" : 298268,\n')
        j.write('\t\t"Strive for Perfection" : 296320,\n')
        j.write('\t\t"Strife" : 304081,\n')
        j.write('\t\t"Ancient Flame" : 295365,\n')
        j.write('\t\t"Reality Shift" : 302916,\n')

        #Special Minors
        j.write('\t\t"Lifeblood 4 Allies" : 295078,\n')
        j.write('\t\t"Lifeblood 3 Allies" : 295078,\n')
        j.write('\t\t"Lifeblood 2 Allies" : 295078,\n')
        j.write('\t\t"Lifeblood 1 Allies" : 295078\n')
        j.write('\t},\n')

        j.write('\t"simulated_steps" :[\n')
        j.write('\t\t"rank_1",\n')
        j.write('\t\t"rank_2",\n')
        j.write('\t\t"rank_3"\n')
        j.write('\t],\n')

        j.write('\t"sorted_data_keys" : [\n')
        DPSDict = dict()
        for u in uniqueList:
            for x in data:
                if x['profile'] == simType and x['actor'] == u+'1':
                    DPSDict.update({u.replace('_',' ').rstrip() : x['DPS']})

        for b in boteList:
            for x in data:
                if x['actor'] == b+'_Uptime_1' and x['profile'] == simType:
                    DPSDict.update({b.replace('_',' ').rstrip() : x['DPS']})

        for l in lifeBloodList:
            for x in data:
                if x['actor'] == l + "_Allies_1" and x['profile'] == simType:
                    name = l.replace('_',' ').rstrip() + ' Allies'
                    DPSDict.update({ name : x['DPS']})

        for w in worldVeinList:
            for x in data:
                if x['actor'] == w + "_Allies_1" and x['profile'] == simType:
                    name = w.replace('_',' ').rstrip() + ' Allies'
                    DPSDict.update({ name : x['DPS']})


        cnt=0
        maxCnt = len(DPSDict)

        import operator
        sorted_x = sorted(DPSDict.items(), key=lambda kv: kv[1], reverse=True)

        for key in sorted_x:
            cnt+=1
            if cnt < maxCnt:
                j.write('\t\t "' + key[0] + '",\n')
            else:
                j.write('\t\t "' + key[0] + '"\n')


        j.write('\t]\n')
        j.write('}')

def buildSingleChart(injsonFile, outjsonFile, simType, sim):
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
        if '' in uniqueList: uniqueList.remove(''); #Remove random blank sims
        ucntMax = len(uniqueList)
        ucnt = 0
        for u in uniqueList:
            if u == "Weapon-Machinist\'s Brilliance":
                j.write('\t\t"Weapon-Machinists Brilliance": {\n')
            else:
                j.write('\t\t"' + u.replace('_',' ').rstrip() +'": {\n')
            ucnt+=1
            for x in data:
                if x['actor'] == u and x['profile'] == simType:
                    j.write('\t\t\t"DPS" : ' + x['DPS'] + '\n')
                    if ucnt < ucntMax:
                        j.write('\t\t},\n')
                    else:
                        j.write('\t\t}\n')
        j.write('\t},\n')
        j.write('\t"simulated_steps" : [\n')
        j.write('\t\t"DPS"\n')
        j.write('\t],\n')
        if sim == 'talents':
            j.write('\t"spell_ids" : {\n')
            # T15
            j.write('\t\t"FotM" : 193195,\n')
            j.write('\t\t"SI" : 162452,\n')
            j.write('\t\t"SWV" : 205351,\n')

            # T45
            j.write('\t\t"ToF" : 109142,\n')
            j.write('\t\t"Mis" : 238558,\n')
            j.write('\t\t"DV" : 263346,\n')

            # T75
            j.write('\t\t"AS" : 155271,\n')
            j.write('\t\t"SWD" : 32379,\n')
            j.write('\t\t"SC" : 205385,\n')

            # T90
            j.write('\t\t"LI" : 199849,\n')
            j.write('\t\t"MB" : 200174,\n')
            j.write('\t\t"VT" : 263165,\n')

            # T100
            j.write('\t\t"LotV" : 193225,\n')
            j.write('\t\t"DA" : 280711,\n')
            j.write('\t\t"STM" : 193223\n')

            j.write('\t},\n')
        if sim == 'enchants':
            j.write('\t"spell_ids" : {\n')
            # Weapon Enchants
            j.write('\t\t"Weapon-Machinists Brilliance" : 298433,\n')
            j.write('\t\t"Weapon-Force Multiplier" : 298440,\n')
            j.write('\t\t"Weapon-Naga Hide" : 298442,\n')
            j.write('\t\t"Weapon-Oceanic Restoration" : 298437,\n')
            j.write('\t\t"Weapon-Torrent of Elements" : 255129,\n')
            j.write('\t\t"Weapon-Deadly Navigation" : 268907,\n')
            j.write('\t\t"Weapon-Masterful Navigation" : 268901,\n')
            j.write('\t\t"Weapon-Quick Navigation" : 268894,\n')
            j.write('\t\t"Weapon-Versatile Navigation" : 268852,\n')

            # Ring Enchantments
            j.write('\t\t"Ring Accord of Haste" : 297989,\n')
            j.write('\t\t"Ring Accord of Critical Strike" : 289009,\n')
            j.write('\t\t"Ring Accorrd of Versatility" : 297993,\n')
            j.write('\t\t"Ring Pact of Haste" : 255076,\n')
            j.write('\t\t"Ring Pact of Critical Strike" : 255075,\n')
            j.write('\t\t"Ring Accord of Mastery" : 297995,\n')
            j.write('\t\t"Ring Pact of Versatility" : 255078,\n')
            j.write('\t\t"Ring Pact of Mastery" : 255077\n')

            j.write('\t},\n')
        if sim == 'consumables':
            j.write('\t"spell_ids" : {\n')
            # Potions/Flasks
            j.write('\t\t"Potion of Unbridled Fury" : 300749,\n')
            j.write('\t\t"Potion of Focused Resolve" : 298744,\n')
            j.write('\t\t"Potion of Rising Death" : 252344,\n')
            j.write('\t\t"Potion of Empowered Proximity" : 298726,\n')
            j.write('\t\t"Superior Battle Potion of Intellect" : 298741,\n')
            j.write('\t\t"Battle Potion of Intellect" : 279162,\n')
            j.write('\t\t"Greater Flask of Endless Fathoms" : 298846,\n')
            j.write('\t\t"Flask of Endless Fathoms" : 252351,\n')

            # Food
            j.write('\t\t"Baked Port Tato" : 168313,\n')
            j.write('\t\t"Mech-Dowels Big Mech" : 168310,\n')
            j.write('\t\t"Swamp Fish n Chips" : 259427,\n')
            j.write('\t\t"Honey-Glazed Haunches" : 259414,\n')
            j.write('\t\t"Bil Tong" : 168314,\n')
            j.write('\t\t"Famine Evaluator and Snack Table " : 297105,\n')
            j.write('\t\t"Abyssal-Fried Rissole" : 168311,\n')
            j.write('\t\t"Fancy Darkmoon Feast" : 185705,\n')
            j.write('\t\t"Spiced Snapper" : 259445,\n')
            j.write('\t\t"Bountiful Captains Feast" : 259421,\n')
            j.write('\t\t"Sailors Pie" : 259439,\n')
            j.write('\t\t"Galley Banquet" : 259418,\n')

            # Rune
            j.write('\t\t"Battle-Scarred Augment Rune" : 270058\n')
            j.write('\t},\n')


        if "Base" in uniqueList: uniqueList.remove("Base")
        j.write('\t"sorted_data_keys":[\n')

        DPSDict = dict()
        for u in uniqueList:
            for x in data:
                if x['profile'] == simType and x['actor'] == u:
                    DPSDict.update({u.replace('_',' ').rstrip() : x['DPS']})

        import operator
        sorted_x = sorted(DPSDict.items(), key=lambda kv: kv[1], reverse=True)
        cnt = 0
        maxCnt = len(sorted_x)
        for key in sorted_x:
            cnt+=1
            if cnt < maxCnt:
                j.write('\t\t "' + key[0] + '",\n')
            else:
                j.write('\t\t "' + key[0] + '"\n')
        j.write('\t]')

        j.write('}')





os.chdir("json_Charts/")




buildTrinketJsonChart(trinketsSCJson, "trinkets_SC_C.json", 'composite')
buildTrinketJsonChart(trinketsSCJson, "trinkets_SC_ST.json", 'single_target')
buildTrinketJsonChart(trinketsSCJsonD, "trinkets_SC_D.json", 'dungeons')
buildTrinketJsonChart(trinketsASJson, "trinkets_AS_C.json", 'composite')
buildTrinketJsonChart(trinketsASJson, "trinkets_AS_ST.json", 'single_target')
buildTrinketJsonChart(trinketsASJsonD, "trinkets_AS_D.json", 'dungeons')
buildTraitJsonChart(traitsSCJson, "traits_SC_C.json", 'composite')
buildTraitJsonChart(traitsSCJson, "traits_SC_ST.json", 'single_target')
buildTraitJsonChart(traitsSCJsonD, "traits_SC_D.json", 'dungeons')
buildTraitJsonChart(traitsASJson, "traits_AS_C.json", 'composite')
buildTraitJsonChart(traitsASJson, "traits_AS_ST.json", 'single_target')
buildTraitJsonChart(traitsASJsonD, "traits_AS_D.json", 'dungeons')


buildTraitJsonComboChart(traitsSCJson, "traits_SC_C_Combo.json", 'composite')
buildTraitJsonComboChart(traitsSCJson, "traits_SC_ST_Combo.json", 'single_target')
buildTraitJsonComboChart(traitsSCJsonD, "traits_SC_D_Combo.json", 'dungeons')
buildTraitJsonComboChart(traitsASJson, "traits_AS_C_Combo.json", 'composite')
buildTraitJsonComboChart(traitsASJson, "traits_AS_ST_Combo.json", 'single_target')
buildTraitJsonComboChart(traitsASJsonD, "traits_AS_D_Combo.json", 'dungeons')

#exit()

buildEssenceJsonChart(essencesASJson, "essences_AS_C.json", 'composite')
buildEssenceJsonChart(essencesSCJson, "essences_SC_C.json", 'composite')
buildEssenceJsonChart(essencesASJson, "essences_AS_ST.json", 'single_target')
buildEssenceJsonChart(essencesSCJson, "essences_SC_ST.json", 'single_target')
buildEssenceJsonChart(essencesASJsonD, "essences_AS_D.json", 'dungeons')
buildEssenceJsonChart(essencesSCJsonD, "essences_SC_D.json", 'dungeons')

buildSingleChart(talentsJson, "talents_C.json", 'composite','talents')
buildSingleChart(talentsJson, "talents_ST.json", 'single_target','talents')
buildSingleChart(talentsJsonD, "talents_D.json", 'dungeons','talents')

buildSingleChart(racialsASJson, "racials_AS_C.json", 'composite','racials')
buildSingleChart(racialsASJson, "racials_AS_ST.json", 'single_target','racials')
buildSingleChart(racialsASJsonD, "racials_AS_D.json", 'dungeons','racials')
buildSingleChart(racialsSCJson, "racials_SC_C.json", 'composite','racials')
buildSingleChart(racialsSCJson, "racials_SC_ST.json", 'single_target','racials')
buildSingleChart(racialsSCJsonD, "racials_SC_D.json", 'dungeons', 'racials')

buildSingleChart(enchantsASJson, "enchants_AS_C.json", 'composite','enchants')
buildSingleChart(enchantsASJson, "enchants_AS_ST.json", 'single_target','enchants')
buildSingleChart(enchantsASJsonD, "enchants_AS_D.json", 'dungeons','enchants')
buildSingleChart(enchantsSCJson, "enchants_SC_C.json", 'composite','enchants')
buildSingleChart(enchantsSCJson, "enchants_SC_ST.json", 'single_target','enchants')
buildSingleChart(enchantsSCJsonD, "enchants_SC_D.json", 'dungeons','enchants')

buildSingleChart(consumablesASJson, "consumables_AS_C.json", 'composite','consumables')
buildSingleChart(consumablesASJson, "consumables_AS_ST.json", 'single_target','consumables')
buildSingleChart(consumablesASJsonD, "consumables_AS_D.json", 'dungeons','consumables')
buildSingleChart(consumablesSCJson, "consumables_SC_C.json", 'composite','consumables')
buildSingleChart(consumablesSCJson, "consumables_SC_ST.json", 'single_target','consumables')
buildSingleChart(consumablesSCJsonD, "consumables_SC_D.json", 'dungeons','consumables')



os.remove(trinketsSCJson)
os.remove(trinketsASJson)
os.remove(traitsSCJson)
os.remove(traitsASJson)
os.remove(trinketsSCJsonD)
os.remove(trinketsASJsonD)
os.remove(traitsSCJsonD)
os.remove(traitsASJsonD)
os.remove(essencesASJson)
os.remove(essencesSCJson)
os.remove(essencesASJsonD)
os.remove(essencesSCJsonD)
os.remove(talentsJson)
os.remove(talentsJsonD)
os.remove(racialsASJson)
os.remove(racialsASJsonD)
os.remove(racialsSCJson)
os.remove(racialsSCJsonD)
os.remove(enchantsASJson)
os.remove(enchantsASJsonD)
os.remove(enchantsSCJson)
os.remove(enchantsSCJsonD)
os.remove(consumablesASJson)
os.remove(consumablesASJsonD)
os.remove(consumablesSCJson)
os.remove(consumablesSCJsonD)




endtime = time.time()
totaltime = endtime-starttime
print("Sucessfully converted charts to JSON format in %d seconds" % (totaltime))
