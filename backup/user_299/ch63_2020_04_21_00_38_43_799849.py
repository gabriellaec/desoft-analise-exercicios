def nome_usuario(string):
    i=0
    for posicao,caractere in enumerate(string):
        if caractere == '@':
            i=posicao
    nome = string[0,i]
            