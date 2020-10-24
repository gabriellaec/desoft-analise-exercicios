def pos_arroba(x):
    i = 0
    while i < len(x):
        if x[i] != '@' :
            i += 1
        else:
            return i
def nome_usuario(x):
    posi = pos_arroba(x)
    nome = x[:posi] 
    return nome