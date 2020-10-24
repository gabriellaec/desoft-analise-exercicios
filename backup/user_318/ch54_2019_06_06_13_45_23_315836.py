def junta_nome_sobrenome(nomes,sobrenomes):
    i=0
    lista=[]
    while i<len(nomes):
        lista.append(nomes[i]+" "+sobrenomes[i])
        i+=1
    return lista
        
        