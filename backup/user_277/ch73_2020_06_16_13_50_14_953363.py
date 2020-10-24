def remove_vogais(string):
    f = len(string)
    i = 0
    k = ''
    while i < f:
        if string[i]!='A' or string[i]!='E' or string[i]!='I' or string[i]!='O' or string[i]!='U':
            k = k+string[i]
        i+=1
    return k