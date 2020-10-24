def junta_nome_sobrenome(lista_nome, lista_sobrenome):
    return ["{0} {1}".format(lista_nome[idx],lista_sobrenome[idx]) for idx, name in enumerate(lista_nome)]