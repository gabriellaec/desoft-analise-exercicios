def calcula_norma(vet):
    for i in vet:
        a = vet[i]
        for c in i:
            b = vet[c]
            norma = (a**2+b**2)**1/2
    return norma