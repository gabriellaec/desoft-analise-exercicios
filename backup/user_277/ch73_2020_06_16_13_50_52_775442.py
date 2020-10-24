def remove_vogais(string):
    f = len(string)
    i = 0
    k = ''
    while i < f:
        if string[i]!='a' or string[i]!='e' or string[i]!='i' or string[i]!='o' or string[i]!='u':
            k = k+string[i]
        i+=1
    return k