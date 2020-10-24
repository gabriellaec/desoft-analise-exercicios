def eh_crescente(lista):
i=0
while i<len(lista):
    if lista[i+1]>lista[i]:
        i+=1
        return True
    else:
        return False