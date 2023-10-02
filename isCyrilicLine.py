import regex as re

# function for determining if line is cyrilic 
def isCyrilicLine(line):
    hasCyrilic = re.search(r'\p{IsCyrillic}', line)
    if (hasCyrilic == None):
        return False 
    else: 
        return True