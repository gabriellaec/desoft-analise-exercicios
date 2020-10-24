def junta_nome_sobrenome(listanome, listasobre):
    listanova=[]
    i=0
    while i<len(listanome):
        espaco= [" "]
        listanova.append(listanome[i] + espaco[0] +listasobre[i])
        i+=1
    return listanova