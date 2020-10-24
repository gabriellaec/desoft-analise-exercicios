def junta_nome_sobrenome(lista_nome,lista_sobrenome):
    lista_pessoa = []
    i = 0
    while i < len(lista_nome):
        lista_pessoa.append(lista_nome[i] + " " + lista_sobrenome[i])
        i += 1
    return lista_pessoa
    