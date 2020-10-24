def eh_crescente(lista):
    lista=[0]*i
    i=0
    while(i<len(lista)):
        if(lista[i+1]>lista[i]):
            return True
        elif(lista[i+1]<=lista[i]):
            return False
        i+=1