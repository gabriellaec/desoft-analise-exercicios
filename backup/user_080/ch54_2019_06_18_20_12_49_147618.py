def junta_nome_sobrenome(lista_nome, lista_sobrenome):
    lista_correta=[]
    for i in len(lista_nome):
        lista_correta.append(lista_nome[i].join(lista_sobrenome[i]))
    return lista_correta
        