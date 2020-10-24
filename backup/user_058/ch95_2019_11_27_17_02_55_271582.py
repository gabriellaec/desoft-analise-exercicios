def mais_populoso(dicionario):
    populacao = {}
    maior_populacao = {}
    maior = 0
    for i in dicionario.keys():
        for k,v in dicionario[i].items():
            if  i not in populacao:
                populacao[i] = v
            elif i in populacao:
                populacao[i] += v
    for k,v in populacao.items():
        if v > maior:
            maior = v
            maior_populacao = {k:v}
    return maior_populacao