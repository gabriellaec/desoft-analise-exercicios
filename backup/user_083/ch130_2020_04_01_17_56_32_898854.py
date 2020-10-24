def monta_mala(lista):
    i=0
    lista=[20,1,4]
    while i<len(lista):
        if sum(lista)>23:
            del lista[i] 
        i+=1
print(lista)
