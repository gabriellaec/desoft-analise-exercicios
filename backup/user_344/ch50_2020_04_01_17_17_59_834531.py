def junta_nome_sobrenome(nomes,sobrenomes):
    i=0
    espaço=[' ']
    while i< len(nomes) and i<len(sobrenomes):
        ni= str(nomes[i]) + str(espaço) + str(sobrenomes[i])
        i+=1
    return ni