f=[]
def zera_negativos(lista):
    i=0
    while i<len(lista):
        if lista[i]>=0:
            f.append(lista[i])
        else:
            f.append(0)
        return
        i+=1    
