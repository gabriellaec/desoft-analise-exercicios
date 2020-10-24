def junta_listas(lista_composta):
    lista_simples=[]
    cont1=0
    cont2=0
    while cont1<len(lista_composta):
        cont2 = 0
        while cont2 < len(lista_composta[cont1]):
            lista_simples.append(lista_composta[cont1][cont2])
            cont2+=1
        cont1+=1
    return lista_simples
