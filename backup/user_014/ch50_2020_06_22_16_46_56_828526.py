def junta_nome_sobrenome (lista_nome, lista_sobrenome):
    lista_nome_sobrenome = []
    i = 0
    while i < len(lista_nome) == len(lista_sobrenome):
        nome_sobrenome = lista_nome[i] + ' ' + lista_sobrenome[i]
        lista_nome_sobrenome.append(nome_sobrenome)
        i += 1
    return lista_nome_sobrenome