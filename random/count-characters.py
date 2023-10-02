import pandas as pd 
import regex as re
import xml.etree.cElementTree as ET 

ns = {"doc": "urn:schemas-microsoft-com:office:spreadsheet"}
tree = ET.parse(r"C:\Projects\master\preprocessing-pipeline\random-files\")
root = tree.getroot()

def getvalueofnode(node):
    return node.text if node is not None else None

def main():
    characterCount = 0
    parsed_xml = tree

    data = []
    for i, node in enumerate(root.findall('.//doc:Row', ns)):
        if i > 6: # this is so we do not insert header row too 
            line = getvalueofnode(node.find('doc:Cell[1]/doc:Data', ns))
            characterCount = characterCount + len(line) + 1
            
    print("Total number of characters: ", characterCount)

main()

