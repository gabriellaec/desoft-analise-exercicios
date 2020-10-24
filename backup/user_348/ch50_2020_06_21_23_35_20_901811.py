def junta_nome_sobrenome(nome, sobrenome):
    # Cria uma lista vazia que será retornada
    resposta = []
    i = 0
    # Determina a condição para o loop
    while len(sobrenome) > i:
        # Cria uma variável com a soma do nome, espaço e sobrenome a cada índice
        nome_completo = nome[i] + ' ' + sobrenome[i]
        # Adiciona a variável na lista que será retornada
        resposta.append(nome_completo)
        i = i + 1
    return resposta