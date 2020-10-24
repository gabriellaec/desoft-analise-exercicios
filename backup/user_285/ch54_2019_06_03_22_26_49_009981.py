def junta_nome_sobrenome(listanome, listasobre):
    listanova=[]
    i=0
    while i<len(listanome):
        lista_vazia= [" "]
        listanova.append(listanome[i] + lista_vazia[0] +listasobre[i])
        i+=1
    return listanova