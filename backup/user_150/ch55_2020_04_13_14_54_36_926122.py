def encontra_maximo(matriz):
    lista = matriz[0]
    maior = lista[0]
    for i in range(len(matriz)):
        a = matriz[i]
        for l in range(len(a)):
            if abs(a[l]) > abs(a[l-1]):
                if abs(a[l]) > maior:
                    maior = abs(a[l])
    return maior