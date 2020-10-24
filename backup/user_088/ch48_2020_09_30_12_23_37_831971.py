def eh_crescente(lista):
    i=0
    while(i<len(lista)):
        if(lista[i+1]>lista[i]):
            return True
        elif(lista[i+1]<=lista[i]):
            return False
        i+=1