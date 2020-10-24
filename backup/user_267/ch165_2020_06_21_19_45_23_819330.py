def mais_populoso(dicio_estados_br):
    lista_estados = []
    lista_habitantes = []
    mais_habitantes = 0
    for estado,dicio_municipios_habitantes in dicio_estados_br.items():
        total = 0
        lista_estados.append(estado)
        for municipio, habitantes in dicio_municipios_habitantes.items():
            total += habitantes
        lista_habitantes.append(total)
    #estado_com_mais = ""
    for i in range(len(lista_habitantes)):
        if lista_habitantes[i] > mais_habitantes:
            mais_habitantes = lista_habitantes[i]
            #estado_com_mais = lista_estados[i]
            indice = i
    return lista_estados[indice]
            
        
        
        