def pos_arroba(palavra):
    k=len(palavra)
    for i in range(0,k):
        if palavra[i]=='@':
            return i
def nome_usuario(palavra):
    i=pos_arroba(palavra)
    f=palavra[0:i]
    return f
    