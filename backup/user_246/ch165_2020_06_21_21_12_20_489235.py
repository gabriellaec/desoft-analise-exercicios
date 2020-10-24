def mais_populoso(p):
    totais = []
    nome = []
    for i in p:
        e = p[i]
        total = 0
        for t in e:
            total += e[t]
        nome.append(e)
        totais.append(total)
    maior = nome[totais.index(max(total))]

    return (maior)
            