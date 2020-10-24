def nome_usuario(email):
    posicao_arroba = email.find('@')
    nome = ''
    for letra in range(0, posicao_arroba):
        nome += email[letra]
    return nome