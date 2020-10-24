def junta_nome_sobrenome(nome,sobrenome):
    contador = 0
    nome_completo = []
    while contador < len(nome):
        nome_completo.append(nome[contador] + " " + sobrenome[contador])
    return nome_completo