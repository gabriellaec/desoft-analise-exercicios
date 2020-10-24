def pos_arroba(a):
    i=0
    while a[i]!='@':
        i+=1
    return i
def nome_usuario(b):
    o=pos_arroba(b)
    return b[:o]