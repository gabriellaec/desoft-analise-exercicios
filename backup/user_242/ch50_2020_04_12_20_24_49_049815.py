def junta_nome_sobrenome(nome,sobrenome):
    lista=[]
    for i in range(1,len(nome)):
        lista.append(nome[i]+' '+ sobrenome[i])
    return lista


