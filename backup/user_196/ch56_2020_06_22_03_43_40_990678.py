def calcula_norma(vet):
    for i in vet:
        a = vet[i]
        b = vet[i+1]
        norma = (a**2+b**2)**1/2
    return norma