def filtra_positivos(lista):
    lista2 = []
    i=0
    for i in lista:
        if i>0:
            lista2.append(i)
        else: 
            lista2=[]
    print (lista2)
