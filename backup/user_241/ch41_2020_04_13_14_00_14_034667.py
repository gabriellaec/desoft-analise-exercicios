lista =[2,6,3,1,49,-4]
def zera_negativos(lista):
    for i in lista:
        if lista[i]<0:
            lista[i]=0
            i+=1
    return(lista)