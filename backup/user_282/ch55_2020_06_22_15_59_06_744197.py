def encontra_maximo(n):
    maior = []
    for i in n:
        for e in range(len(n)):
            x = abs(i[e])
            maior.append(x)
    return max(maior)