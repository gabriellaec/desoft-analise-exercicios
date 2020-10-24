def junta_nome_sobrenome(nomes,sobrenomes):
    lista=[]
    for i in range(len(nomes)):
        lista.append(nomes[i]+' '+sobrenomes[i])
    return lista
