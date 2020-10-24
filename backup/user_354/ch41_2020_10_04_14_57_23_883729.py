i=0
while i<len(lista):
    if lista[i]>=0:
        lista.append(lista[i])
    else:
        lista.append(0)
    i+=1    
