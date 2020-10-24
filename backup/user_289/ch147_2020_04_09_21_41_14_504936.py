def mais_frequente(lista):
    def conta_ocorrencias(lista):
        dicionario = {}
        for i in lista:
            if not i in dicionario:
                dicionario[i] = 1
            else:
                dicionario[i] += 1
    todos_values = dicionario.values()
    maior_value = max(todos_values)
    return dicionario[i] with maior_value