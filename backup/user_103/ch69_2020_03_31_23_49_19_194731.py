def junta_listas(lista):
    lista1=[]
    i=0
    while i< len(lista):
        lista1.append((lista[i].strip('[]')))
        i+=1
        
    print (lista1)