def pos_arroba(s):
    l = list(s)
    i = 0
    k = 0
    while i<len(l):
        if l[i] == '@':
            k = i
        i+=1
    return k
def nome_usuario(e):
    w = pos_arroba(e)
    return e[:w]
    
    