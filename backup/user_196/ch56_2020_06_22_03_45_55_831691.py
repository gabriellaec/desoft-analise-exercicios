def calcula_norma(vet):
    for i in vet:
        for c in i:
            a = vet[c]
            b = vet[c+1]
            norma = (a**2+b**2)**1/2
    return norma