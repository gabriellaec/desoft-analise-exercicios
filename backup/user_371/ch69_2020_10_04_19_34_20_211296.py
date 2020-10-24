def junta_listas(listas):
    i=0
    lista_nova=[]
    while i<len(listas):
        lista_nova=listas[i]+lista_nova
        i+=1
    return lista_nova