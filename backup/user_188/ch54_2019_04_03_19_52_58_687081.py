def junta_nome_sobrenome(nome, sobrenome):
    contador = 0
    nome_sobrenome = []
    while contador < len(nome):
        nome_sobrenome.append(nome[contador] + " " + sobrenome[contador])
        contador += 1
    return nome_sobrenome