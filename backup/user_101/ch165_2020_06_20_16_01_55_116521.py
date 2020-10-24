def mais_populoso(d):
    for estado in d.items():
        soma = 0
        maior_soma = 0
        mais_populoso = 0
        for pop_cidade in estado[1].values():
            soma += pop_cidade[1]
        if soma > maior_soma:
            maior_soma = soma
            mais_populoso = estado[0]