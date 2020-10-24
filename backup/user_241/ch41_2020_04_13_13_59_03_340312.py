lista =[2,6,3,1,49,-4]
def zera_negativos(lista):
    for i in lista:
        if lista[0]<0:
            lista[0]=0
            i+=1
    return(lista)