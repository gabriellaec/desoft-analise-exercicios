def encontra_maximo(matriz):
    lista=[]
    for i in matriz:
        lista.append(maximum(i))
    return maximum(lista)

def maximum(lista):
    for i in range(len(lista)):
        if i==0:
            m=lista[i]
        elif m<lista[i]:
            m=lista[i]