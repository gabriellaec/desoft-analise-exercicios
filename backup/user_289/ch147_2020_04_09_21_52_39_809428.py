def mais_frequente(lista):
    def conta_ocorrencias(lista):
        dicionario = {}
        for i in lista:
            if not i in dicionario:
                dicionario[i] = 1
            else:
                dicionario[i] += 1
    for value in dicionario.values():
        if value >= dicionario.values():
            value = maior_valor
    return maior_value