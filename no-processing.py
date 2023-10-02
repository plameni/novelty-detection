import pandas as pd 
import xml.etree.cElementTree as ET 

ns = {"doc": "urn:schemas-microsoft-com:office:spreadsheet"}
tree = ET.parse(r"C:\Users\apl\Projects\preprocesing-pipeline\full-preprocessing\new-test\full-data\forbidden.xml")
root = tree.getroot()

def getvalueofnode(node):
    # return node text or None 
    return node.text if node is not None else None

def main():
    counter = 1
    parsed_xml = tree

    data = []
    for i, node in enumerate(root.findall('.//doc:Row', ns)):
        line = getvalueofnode(node.find('doc:Cell[1]/doc:Data', ns))
        with open('./new-test/no-processing/forbidden/' + str(counter) + '.txt', 'w', encoding="utf-8") as generatedTxtFile: 
            generatedTxtFile.write(str(line))
            counter = counter + 1

main()

