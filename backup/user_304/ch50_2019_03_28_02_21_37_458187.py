def numero_no_indice (lista):
    indice=[]
    i=0   
    while i<len(lista):
        i+=1
        if lista[i]==i:
            indice.append (i)
            