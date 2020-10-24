def eh_crescente(lista):
    i=0
    while i<len(lista)-1:
        if lista[i+1]>lista[i]:
            return True
        if lista[i+1]<=lista[i]:
            return False
        i+=1
        