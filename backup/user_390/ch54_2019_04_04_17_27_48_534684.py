def junta_nome_sobrenome(nome, sobrenome):
    i=0
    listanova=[]
    while i<len(nome):
        listanova.append(nome[i] and sobrenome[i])
        i+=1
    return listanova
                         