import xml.etree.cElementTree as ET 
import json
import types
import copy
import os

# imports of custom implemented functions
from isCyrilicLine import isCyrilicLine
from replaceSpecialChars import replaceSpecialChars
from removeHtmlEntitites import removeHtmlEntities
from translate import translate
from toLower import toLower
from removePunctuation import removePunctuation 
from removeWordsShorterThan3 import removeWordsShorterThan3
from deduceWordRoot import deduceWordRoot
from filterByRegex import filterByRegex

ns = {"doc": "urn:schemas-microsoft-com:office:spreadsheet"}
tree = ET.parse(r"C:\Users\apl\Projects\preprocesing-pipeline\full-preprocessing\new-test\full-data\forbidden.xml")
# tree = ET.parse(r"C:\Projects\master\preprocessing-pipeline-full\preprocesing-pipeline\random-files\forbidden.xml")
root = tree.getroot()

# output_folder = input("insert output folder path\n")

def cloneAndCopyList(allConfigs): 
    configLength = len(allConfigs)
    for i in range(0, configLength):
        configToAppend = allConfigs[i]
        newConfig = copy.deepcopy(configToAppend)
        allConfigs.append(newConfig)
        
def getFolderName(config):
    folderName = ''
    for key in config.__dict__:
        if key == 'removeHtmlEntities':
            folderName = folderName + 'rhe'
        if key == 'translate':
            folderName = folderName + 't'
        if key == 'replaceSpecialChars':
            folderName = folderName + 'rsc'
        if key == 'toLower':
            folderName = folderName + 'l'
        if key == 'removeCyrilic':
            folderName = folderName + 'c'
        if key == 'removePunctuation':
            folderName = folderName + 'rp'
        if key == 'removeWordsShorterThan3': 
            folderName = folderName + 'rws'
        if key == 'filterByRegex': 
            folderName = folderName + 'fbr'
        if key == 'deduceWordRoot': 
            folderName = folderName + 'wr'
        if config.__dict__[key] == True: 
            folderName = folderName + '1'
        else: 
            folderName = folderName + '0'
    return folderName

def getvalueofnode(node):
    return node.text if node is not None else None

def main():
    
    # loading configurations in json 
    """
    f = open('runningConfigurations.json')
    jsonConfigData = json.load(f)
    runningConfigurations = jsonConfigData['configurations']
    
    #preparing all possible confs
    dummyConfig = types.SimpleNamespace()
    allConfigs = []
    allConfigs.append(dummyConfig) 
    
    for i in range(0, len(runningConfigurations)):
        currentConfig = runningConfigurations[i]
        if (currentConfig['configValueType'] == 'bool'):
            cloneAndCopyList(allConfigs)
            for j in range(0, len(allConfigs)):
                if (j < len(allConfigs) / 2):
                    setattr(allConfigs[j], currentConfig['propertyName'], True)
                else: 
                    setattr(allConfigs[j], currentConfig['propertyName'], False)
    """
            

    # loading data
    completeData = []
    for i, node in enumerate(root.findall('.//doc:Row', ns)):
        if i > 0: # this is so we do not insert header row too, but for now, no header
            line = getvalueofnode(node.find('doc:Cell[1]/doc:Data', ns))
            completeData.append(line)
            
    # configs and data are ready, now to process the data according to each conf 
    
    lineCounter = 1
    for j in range(0, len(completeData)): 
        line = completeData[j]
        line = translate(line)
        if not line == False:
            line = replaceSpecialChars(line)
            line = removeHtmlEntities(line)
            line = removePunctuation(line)
            line = removeWordsShorterThan3(line)
            line = toLower(line)
            with open('new-test/full-data-preprocessing/forbidden/' + str(lineCounter) + '.txt', 'w', encoding="utf-8") as generatedTxtFile: 
                generatedTxtFile.write(str(line))
                lineCounter = lineCounter + 1
    
main()