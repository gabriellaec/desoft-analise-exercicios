def junta_nome_sobrenome(nomes,sobrenomes):
    i=0
    ni = []
    while i< len(nomes) and i<len(sobrenomes):
        ni.append( nomes[i] + " " + sobrenomes[i])
        i+=1
    return ni