from bs4 import BeautifulSoup

def removeHtmlEntities(line):
    line = BeautifulSoup(line, features="lxml")
    return line.text