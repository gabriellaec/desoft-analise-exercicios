def encontra_maximo(lista):
    maior = lista[0][0]
    for i in range(0, len(lista)):
        for a in lista[i]:
            if a < 0:
                a *= -1
            if a > maior:
                maior = a
            
    return maior
    