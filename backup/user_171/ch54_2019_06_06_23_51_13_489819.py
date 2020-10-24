def junta_nome_sobrenome(nome,sobrenome):
    lista=[]
    for i in range(len(nome)):
        for s in range(len(nome)):
            lista.append(nome[i]+' '+nome[s])
    return lista
