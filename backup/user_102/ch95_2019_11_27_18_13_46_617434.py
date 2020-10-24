def mais_populoso(x):
    for i, e in x.items():
        Populacao = []
        for key, values in e.items():
            Populacao.append(values)
    pop = 0
    pop2 = []
    for t in Populacao:
        t += pop
        pop2.append(pop)
    if pop2[0] > pop2[1]:
        return("Sao Paulo")
    else:
        return("Minas Gerais")