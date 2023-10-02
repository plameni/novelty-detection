import pandas as pd 
import regex as re
import xml.etree.cElementTree as ET 
import string 

from bs4 import BeautifulSoup
from googletrans import Translator


ns = {"doc": "urn:schemas-microsoft-com:office:spreadsheet"}
tree = ET.parse(r"C:\Projects\master\preprocessing-pipeline\random-files\test.xml")
root = tree.getroot()
translator = Translator()

output_folder = input("insert output folder path\n")

def getvalueofnode(node):
    return node.text if node is not None else None

def isCyrilicLine(line):
    hasCyrilic = re.search(r'\p{IsCyrillic}', line)
    if (hasCyrilic == None):
        return False 
    else: 
        return True

# dodati opciju sve u mala/velika slova
def lineToLower(line): 
    line = str.lower(line)
    return line

# ukloniti interpunkciju 
def removePunctuation(line):
    line = line.translate(str.maketrans("",""))
    return line
    
# rijeci krace od tri slova 
def removeWordsShorterThan3(line): 
    line = re.sub(r'\b\w{1,3}\b', '',line)
    return line

# filtriranje po regularnim izrazima (za ovo gore)


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
    # Da napravimo konfigurabilno (u smislu š mozemo da prevedemo i u s
    # i u sh)- json fajl sa konfiguracijom, odakle cita mapu 
    return line

def removeHtmlEntities(line):
    line = BeautifulSoup(line, features="lxml")
    return line.text

def translateLine(line): 
    result = translator.translate(line, dest='en', src='sr')
    return result.text

def main():
    counter = 1
    cyrilicCounter = 0
    parsed_xml = tree

    data = []
    for i, node in enumerate(root.findall('.//doc:Row', ns)):
        if i >= 0: # this is so we do not insert header row too, but for now, no header 
            line = getvalueofnode(node.find('doc:Cell[1]/doc:Data', ns))
            if not isCyrilicLine(line):
                line = replaceSpecialChars(line)
                # for some reason, when we are translating here firstly we remove 
                # html entities, and that do translate
                # in the other variant, we firstly need to translate
                # then remove html entitites
                line = removeHtmlEntities(line)
                line = translateLine(line)
                line = lineToLower(line)
                line = removePunctuation(line)
                line = removeWordsShorterThan3(line)
                with open('./../random-files/generated-text-files/' + output_folder + "/" + str(counter) + '.txt', 'w', encoding="utf-8") as generatedTxtFile: 
                    generatedTxtFile.write(str(line))
                    counter = counter + 1
            else: 
                print(line) # This line is just for testing 
                cyrilicCounter = cyrilicCounter + 1
            
    print("Removed ", cyrilicCounter, " cyrilic comments")

main()

