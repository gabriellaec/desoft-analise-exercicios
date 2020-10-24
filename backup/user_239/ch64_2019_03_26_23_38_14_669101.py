def pos_arroba(x):
    i=0
    while i<len(x):
        if x[i]=='@':
            a=i
        i+=1
    return a
def nome_usuario(x):
    n=pos_arroba(x)
    k=(x[:n])
    return k