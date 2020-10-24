def encontra_maximo(lista_matriz):
    maior = 0
    for i in lista_matriz:
        for n in i:
            if n > maior:
                maior = n
    return maior