def inverte_lista(lista):
    inv=[]
    x=len(lista)
    i=0
    while i<x:
        inv.append(lista[x-i-1])
        i+=1
    print(inv)
    return inv