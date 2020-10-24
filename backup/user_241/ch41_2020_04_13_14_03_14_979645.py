lista =[2,6,3,1,49,-4]
def zera_negativos(lista):
    i=0
    for i in len(lista):
        if lista[i] < 0:
            lista[i]=0
            i+=1
    return lista