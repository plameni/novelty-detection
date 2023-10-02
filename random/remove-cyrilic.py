import pandas as pd 
import regex as re
import xml.etree.cElementTree as ET 

ns = {"doc": "urn:schemas-microsoft-com:office:spreadsheet"}
tree = ET.parse(r"C:\Projects\master\preprocessing-pipeline\random-files\test.xml")
root = tree.getroot()

output_folder = input("insert output folder path\n")

def getvalueofnode(node):
    return node.text if node is not None else None

def main():
    counter = 1
    cyrilicCounter = 0
    parsed_xml = tree

    data = []
    for i, node in enumerate(root.findall('.//doc:Row', ns)):
        if i > 6: # this is so we do not insert header row too 
            line = getvalueofnode(node.find('doc:Cell[1]/doc:Data', ns))
            hasCyrilic = re.search(r'\p{IsCyrillic}', line)
            if (hasCyrilic == None):
                with open('./../random-files/generated-text-files/' + output_folder + "/" + str(counter) + '.txt', 'w', encoding="utf-8") as generatedTxtFile: 
                    generatedTxtFile.write(str(line))
                    counter = counter + 1
            else: 
                print(line) # This line is just for testing 
                cyrilicCounter = cyrilicCounter + 1
            
    print("Removed ", cyrilicCounter, "comments")

main()

