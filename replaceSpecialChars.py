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