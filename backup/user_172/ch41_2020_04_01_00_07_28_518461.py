def zera_negativos (lista):
    lista=[]
    for i in lista:
        if i<0:
            del(i)
        else:
            listanova.append(i)
            
    return listanova