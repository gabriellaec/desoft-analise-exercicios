def numero_digitos(s):
    i=0
    d=0
    while i in s:
        if s[i].isdigit() == True:
            d+=1
            i+=1
        else:
            i+=1