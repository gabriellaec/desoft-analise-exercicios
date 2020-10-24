def junta_nome_sobrenome(lista_nome,lista_sobrenome):
    i=0
    lista_nomes = []
    while i < len(lista_nome):
        lista_nomes.append(lista_nome[i] + ' ' + lista_sobrenome[i])
        i+=1
    return lista_nomes