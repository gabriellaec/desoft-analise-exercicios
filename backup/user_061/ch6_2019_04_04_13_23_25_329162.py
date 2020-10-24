
def encontra_maximo(matriz):
    maior_valor = -1000000000000000000000
    i = 0
    while i<len(matriz):
        lista = matriz[i]
        f = 0
        while f<len(lista):
            if maior_valor < lista[f]:
                maior_valor = lista[f]
            f+=1
        i+=1
    return maior_valor