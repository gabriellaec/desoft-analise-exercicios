def zera_negativos(lista):
    lista2=[]
    for i in lista:
        if i<0:
            i=0
            lista2.append(i)
        else:
            lista2.append(i)