def mais_frequente(lista):
    dicionario = {}
    def conta_ocorrencias(lista):
        dicionario = {}
        for i in lista:
            if not i in dicionario:
                dicionario[i] = 1
            else:
                dicionario[i] += 1
    maior_key = max(dicionario, key =dicionario.get)
    return maior_key