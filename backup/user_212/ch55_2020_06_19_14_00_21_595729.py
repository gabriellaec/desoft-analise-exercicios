def encontra_maximo(matriz):
    lista=[]
    for linha in matriz:
        for e in linha:
            valor = abs(e)
            lista.append(valor)
    maior = max(lista)
    return maior 