def verifica_progressao(lista):
    a=lista[1]-lista[0]
    pa=True
    for e in range(len(lista)):
        x=lista[e-1]-lista[e]
        if x!=a:
            pa=False
            