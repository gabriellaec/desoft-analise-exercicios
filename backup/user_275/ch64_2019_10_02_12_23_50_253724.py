def pos_arroba(E):
    i=0
    n=len(E)
    while i<n:
        if E[i] == '@':
            resultado= i
        i+=1
    return resultado

def nome_usuario(T):
    final=pos_arroba(T)
    usuario=T[0:final]
    return usuario