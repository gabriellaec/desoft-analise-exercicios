def mais_populoso(dic):
    maior_populacao = 0
    maior_estado = ''
    for e in dic:
        populacao = 0
        for m, p in dic[e].items():
            populacao += p
            if populacao > maior_populacao:
                maior_populacao = populacao
                maior_estado = e
    return maior_estado