def removePunctuation(line):
    line = line.translate(str.maketrans("",""))
    return line