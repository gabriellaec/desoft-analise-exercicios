def pos_arroba(email):
    i = 0
    while i < len(email):
        if email[i] == '@':
            return i
        i = i + 1

def nome_usuario(email):
    # Cria uma variável com a função que determina a posição do @
    f = pos_arroba(email)
    # Cria uma variável que determina o nome (vai do começo da sting até o índice antes da posição do @)
    nome = email[0:f]
    return nome