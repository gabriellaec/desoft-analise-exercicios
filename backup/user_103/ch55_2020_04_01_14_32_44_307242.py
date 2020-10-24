def encontra_maximo(matriz):
    i=0
    lista1=[matriz[0]]
    lista2=[matriz[1]]
    lista3=[matriz[3]]
    listamaior1=[]
    listamaior2=[]
    listamaior3=[]
    while i<len(lista1):
        if lista1[i+1]>lista1[i]:
            listamaior1.append(lista1[i+1])
            i+=1
        if  lista2[i+1]>lista2[i]:
            listamaior2.append(lista2[i+1])
            i+=1
        if  lista3[i+1]>lista3[i]:
            listamaior3.append(lista3[i+1])
            i+=1
        listafinal=listamaior1+listamaior2+listamaior3
    print (max(listafinal))
    
    
                               
        