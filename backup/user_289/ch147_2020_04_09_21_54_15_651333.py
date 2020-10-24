def mais_frequente(lista):
    dicionario = {}
        for i in lista:
            if not i in dicionario:
                dicionario[i] = 1
            else:
                dicionario[i] += 1
    for value in dicionario.values():
        if value >= dicionario.values():
            value = maior_valor
    return maior_valor