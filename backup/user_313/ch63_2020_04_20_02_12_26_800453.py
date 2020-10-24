def pos_arroba(n):
    for i in range(0,len(n)):
        if n[i] == '@':
            return i
        
def nome_usuario(a):
    numero = pos_arroba(a)
    resposta = a[:numero]
    return resposta