def encontra_maximo(matriz):
    if matriz==[]:
        return []
    else:
        lista1=[matriz[0]]
        lista2=[matriz[1]]
        lista3=[matriz[2]]
        listamaior1=max(lista1)
        listamaior2=max(lista2)
        listamaior3=max(lista3)
        listafinal=[listamaior1,listamaior2,listamaior3]
        maior=max(listafinal)
    print(listamaior1)
    print (maior)    
    print (matriz)
                               
        