def monta_mala(lista_de_pesos):
    i=0 
    peso_total=0 #variavel que guarda o encremento do peso das malas despachadas
    lista_de_despache=[] #lista de malas que seram despachadas
    while i<len(lista_de_pesos):
        peso_total+=lista_de_pesos[i]
        if peso_total<=23:
            lista_de_despache.append(lista_de_pesos[i])
        else:
            break
        i+=1
    return lista_de_despache
            