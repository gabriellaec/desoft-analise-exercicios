with open('macacos-me-mordam.py','r') as arquivo:
    lines=arquivo.readline()
    for line in lines:
        lines=arquivo.readline()
        arroz=line.split(',')