def inverte_lista(lista):
    i=0
    j=len(lista)
    nova_lista=[]
    while len(nova_lista)!=len(lista):
        nova_lista.append(lista[j-1])
        i+=1
        j-=1
    return nova_lista
print(inverte_lista([1,2,3,4,5,6,7,8,9]))