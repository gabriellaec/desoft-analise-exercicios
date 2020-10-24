def mais_populoso(d):
    soma = 0
    maior_soma = 0
    mais_populoso = 0
    for estado in d.items():
        for pop_cidade in estado[1].values():
            soma += pop_cidade
        if soma > maior_soma:
            maior_soma = soma
            mais_populoso = estado[0]
    return mais_populoso