import pandas as pd 
import xml.etree.cElementTree as ET 

ns = {"doc": "urn:schemas-microsoft-com:office:spreadsheet"}
tree = ET.parse(r"C:\Projects\master\preprocessing-pipeline\random-files\test.xml")
root = tree.getroot()

output_folder = input("insert output folder path\n")

def getvalueofnode(node):
    # return node text or None 
    return node.text if node is not None else None

def main():
    counter = 1
    parsed_xml = tree

    data = []
    for i, node in enumerate(root.findall('.//doc:Row', ns)):
        #line = {'account': getvalueofnode(node.find('doc:Cell[1]/doc:Data', ns)),
        #            'total': getvalueofnode(node.find('doc:Cell[2]/doc:Data', ns))}
        line = getvalueofnode(node.find('doc:Cell[1]/doc:Data', ns))
        #print(line)
        with open('./../random-files/generated-text-files/' + output_folder + "/" + str(counter) + '.txt', 'w', encoding="utf-8") as generatedTxtFile: 
            generatedTxtFile.write(str(line))
            counter = counter + 1
        # data.append(line)
            

    # return(pd.DataFrame(data))

main()

