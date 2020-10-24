def mais_populoso(dicio_brasil):
    lista_estados=[]
    lista_pop=[]
    for estados,mun_pop in dicio_brasil.items():
        lista_estados.append(estados)
        #print(estados)
        lista_pop_mun=[]
        for pop in mun_pop.values():
            lista_pop_mun.append(pop)
            #print(pop)
        lista_pop.append(sum(lista_pop_mun))
    #print(lista_pop)
    maior_pop=max(lista_pop)
    indice=lista_pop.index(maior_pop)
    return lista_estados[indice]
