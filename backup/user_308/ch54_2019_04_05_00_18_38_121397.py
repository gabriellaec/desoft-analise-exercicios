def junta_nome_sobrenome(nomes,sobre):
    listaf=[]
    i=0
    while contador<len(sobre):
        listaf.append("{0} {1}".format(nomes[i],sobre[i]))
        i+=1
    return listaf     