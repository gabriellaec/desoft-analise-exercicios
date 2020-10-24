def  inverte_lista(lista):
    invertida = []
    i = len(invertida)-1
    while i>=0:
        invertida.append(inverte_lista[i])
        i-=1    
    print (invertida)
    