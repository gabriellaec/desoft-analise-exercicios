def junta_nome_sobrenome(listanome, listasobre):
    listanova=[]
    i=0
    while i<len(listanome):
        listanova.append(listanome[i] + listasobre[i])
        i+=1
    return listanova
        