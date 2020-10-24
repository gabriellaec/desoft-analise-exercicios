def pos_arroba(email):
    email2 = str(email)
    posicao = 0
    for i in email2:
        if i == '@':
            return posicao
        posicao += 1
    
def nome_usuario(string):
    texto = pos_arroba(string)
    
    return (string[:texto])
