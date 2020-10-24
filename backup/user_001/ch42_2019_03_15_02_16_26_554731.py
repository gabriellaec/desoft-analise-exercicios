def quantos_uns(x):
    s=str(x)
    cont=len(s)
    r=01
    while cont>0:
        cont=cont-1
        if s[cont]=="1":
            r=r+1
    return r
