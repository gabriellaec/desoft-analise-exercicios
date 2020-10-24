def numero_digitos(s):
    d=0
    for i in s:
        if s[i].isdigit() == True:
            d+=1
    return d