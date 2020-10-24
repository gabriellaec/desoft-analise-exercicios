def faixa_notas(lista):
    lista1=[]
    lista2=[]
    lista3=[]
    a=len(lista1)
    b=len(lista2)
    c=len(lista3)
    listaf=[a,c,b]
    x=0
    while x<len(lista):
        if lista[x]<5:
            lista1.append(x)
        elif lista[x]>7:
            lista3.append(x)
        else:
            lista2.append(x)
        x+=1
    return listaf