def junta_listas(listas):
    i=(len(listas)-1)
    lista_nova=[]
    while i>=0:
        lista_nova=listas[i]+lista_nova
        i-=1
    return lista_nova