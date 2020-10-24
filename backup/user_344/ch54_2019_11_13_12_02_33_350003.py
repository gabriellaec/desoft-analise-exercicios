def junta_nome_sobrenome(nomes,sobrenomes):
    i=0
    espaço=[' ']
    while i< len(nomes):
        ni= nomes[i] + espaço + sobrenomes[i]
        i+=1
    return ni