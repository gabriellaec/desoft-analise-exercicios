def junta_nome_sobrenome(x, y):
    nomes = []
    i = 0
    espaco = " "
    while i < len(x):
        nome = x[i] + espaco + y[i]
        nomes.append(nome)
        i += 1
    return nomes
