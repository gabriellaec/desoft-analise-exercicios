lista=[]
nova_lista=[]
def monta_mala(lista):
    i=0
    s=lista[i]
    while s<=23:
        i+=1
        s+=lista[i]
        nova_lista.append(s)
    return nova_lista
    
