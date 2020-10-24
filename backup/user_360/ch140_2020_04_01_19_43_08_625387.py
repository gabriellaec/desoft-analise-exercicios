def faixa_notas(lista):
    lista1=[]
    lista2=[]
    lista3=[]
    x=0
    while x<len(lista):
        listaf=[len(lista1),len(lista3),len(lista2)]
        if lista[x]<5:
            lista1.append(x)
        elif lista[x]>7:
            lista2.append(x)
        else:
            lista3.append(x)
        x+=1
    return listaf