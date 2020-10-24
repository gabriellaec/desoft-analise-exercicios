def monta_mala(lista_de_pesos):
    i=0
    peso_total
    lista_de_despache=[]
    while i<len(lista_de_pesos)-1:
        peso_total+=lista_de_pesos[i]
        if peso_total<=23:
            lista_de_despache.append(lista_de_pesos[i])
        else:
            break
        i+=1
    return lista_de_despache
            