def junta_nome_sobrenome(nome, sobrenome):
    contador = 0
    nome_sobrenome = []
    while contador < len(nome):
        nome_sobrenome[contador] = nome[contador] + " " + sobrenome[contador]
    return nome_sobrenome