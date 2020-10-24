def calcula_norma(x):
    lista=[]
    for e in x:
        lista.append(e**2)
    v=(sum(lista)**(1/2))
    return v 