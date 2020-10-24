def apaga_repetidos(string):
    stringfinal = ''    
    string2 = []
    asterisco = 0
    for i in string2:
        if i.upper() not in string2:
            string2.append(i.upper())
        else:
            asterisco = '*'
        stringfinal += asterisco
    return stringfinal