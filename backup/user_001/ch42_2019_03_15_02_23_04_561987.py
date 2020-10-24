def quantos_uns(x):
    s=str(x)
    cont=0
    r=0
    while cont<len(s):
        if s[cont]=="1":
            r+=1
        cont+=1
    return r
