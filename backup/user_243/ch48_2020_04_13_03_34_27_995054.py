def eh_crescente(lista)
i=0
while len(lista)>i:
    if lista[i]>lista[i-1]:
        return True
    else:
        return False
    i+=1