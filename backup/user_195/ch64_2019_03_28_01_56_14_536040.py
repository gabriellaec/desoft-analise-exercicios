def pos_arroba(p):
    r=0
    i=0
    while i<len(p):
        if p[i]=="@":
            r=i
        i+=1
    return r

def nome_usuario(p):
    a=pos_arroba(p)
    return p[ :a]