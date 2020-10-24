lista=[]
nova_lista=[]
def monta_mala(lista):
    i=0
    s=0
    while s<23:
        s=lista[i]+lista[i+1]
        nova_lista.append(lista[i],lista[i+1])
        i+=1
    return nova_lista
    
