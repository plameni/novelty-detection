import pandas as pd 
import regex as re
import xml.etree.cElementTree as ET 
from bs4 import BeautifulSoup

import json
import requests

ns = {"doc": "urn:schemas-microsoft-com:office:spreadsheet"}
tree = ET.parse(r"C:\Projects\master\preprocessing-pipeline\random-files\test.xml")
root = tree.getroot()

output_folder = input("insert output folder path\n")

#loading necessary api keys 
apiKeysFile = open('./../api-keys.json')
apiKeysData = json.load(apiKeysFile)
googleTranslateApiKey = apiKeysData['google-translate-api-key']

def getvalueofnode(node):
    return node.text if node is not None else None

def isCyrilicLine(line):
    hasCyrilic = re.search(r'\p{IsCyrillic}', line)
    if (hasCyrilic == None):
        return False 
    else: 
        return True

def replaceSpecialChars(line):
    line = line.replace('č', 'c')
    line = line.replace('ć', 'c')
    line = line.replace('ž', 'z')
    line = line.replace('đ', 'dj')
    line = line.replace('š', 's')
    line = line.replace('Č', 'C')
    line = line.replace('Ć', 'C')
    line = line.replace('Ž', 'Z')
    line = line.replace('Đ', 'Dj')
    line = line.replace('Š', 'S')
    return line

def removeHtmlEntities(line):
    line = BeautifulSoup(line, features="lxml")
    return line.text

def translateLine(line): 
    queryParams = { 'key': googleTranslateApiKey }
    data = { 'q':line, 'source':'sr', 'target':'en' }
    url = 'https://translation.googleapis.com/language/translate/v2'
    response = requests.post(url, params=queryParams, data=data)
    response = json.loads(response.text)
    translatedText = response['data']['translations'][0]['translatedText']
    return translatedText

def main():
    counter = 1
    cyrilicCounter = 0
    parsed_xml = tree

    data = []
    for i, node in enumerate(root.findall('.//doc:Row', ns)):
        if i >= 0: # this is so we do not insert header row too 
            line = getvalueofnode(node.find('doc:Cell[1]/doc:Data', ns))
            if not isCyrilicLine(line):
                line = replaceSpecialChars(line)
                line = translateLine(line)
                line = removeHtmlEntities(line)
                with open('./../random-files/generated-text-files/' + output_folder + "/" + str(counter) + '.txt', 'w', encoding="utf-8") as generatedTxtFile: 
                    generatedTxtFile.write(str(line))
                    counter = counter + 1
            else: 
                print(line) # This line is just for testing 
                cyrilicCounter = cyrilicCounter + 1
            
    print("Removed ", cyrilicCounter, " cyrilic comments")

main()

