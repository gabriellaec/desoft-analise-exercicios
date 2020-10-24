lista=[]
nova_lista=[]
def monta_mala(lista):
    i=0
    s=lista[i]
    while s<=23:
        s+=lista[i+1]
        nova_lista.append(lista[i])
        nova_lista.append(lista[i+1])
        i+=1
    return nova_lista
    
