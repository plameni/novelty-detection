import re
def filterByRegex(line, regexText):
    line = re.sub(regexText, '', line)
    return line