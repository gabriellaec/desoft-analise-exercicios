def junta_nome_sobrenome(listanome, listasobre):
    listanova=[]
    lista_vazia=[" "]
    i=0
    while i<len(listanome):
        listanova.append(listanome[i] + lista_vazia[i] +listasobre[i])
        i+=1
    return listanova
print(junta_nome_sobrenome(["kamila"],["wansa"]))