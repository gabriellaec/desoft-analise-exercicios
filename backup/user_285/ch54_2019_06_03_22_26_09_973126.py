def junta_nome_sobrenome(listanome, listasobre):
    listanova=[]
    i=0
    while i<len(listanome):
        lista_vazia= [" "]
        listanova.append(listanome[i] + lista_vazia[0] +listasobre[i])
        i+=1
    return listanova

def junta_nome_sobrenome(listanome,listasobre):
    i=0
    z=[]*len(listanome)
    while i < len(listanome):
        z.append("{0} {1}".format(listanome[i], listasobre[i])
        i+=1
    return z