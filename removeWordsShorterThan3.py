import re
def removeWordsShorterThan3(line): 
    line = re.sub(r'\b\w{1,3}\b', '',line)
    return line
