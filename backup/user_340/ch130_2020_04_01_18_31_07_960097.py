lista=[]
nova_lista=[]
def monta_mala(lista):
    i=0
    s=lista[i]
    if s<=23:
        nova_lista.append(s)
    while s<=23:
        i+=1
        s+=lista[i]
    if s>23:    
    return nova_lista
    
