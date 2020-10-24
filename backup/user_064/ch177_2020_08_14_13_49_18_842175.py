def numero_digitos(s):
    d=0
    for i in s:
        if i.isdigit() == True:
            d+=1
            print(s[i])
    return d 