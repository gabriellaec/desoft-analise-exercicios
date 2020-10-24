def mais_populoso(dicionario):
    max_pop = 0
    soma = 0
    for i in dicionario:
        for a in dicionario[i]:
            soma += dicionario[i[a]]
            if soma > max_pop:
                soma = max_pop
                estado_mais_pop = dicionario[i]
    return estado_mais_pop