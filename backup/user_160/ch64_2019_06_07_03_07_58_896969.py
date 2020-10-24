def pos_arroba(n):
    for i in range(0,len(n)):
        if n[i] == "@":
            return i
def nome_usuario(n):
    a = pos_arroba(n)
    nome = n[0:(a)]
    return nome
        
    