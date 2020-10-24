def junta_nome_sobrenome(lista_nome, lista_sobrenome):
    lista_completa = ["{0} {1}".format(lista_nome[idx],lista_sobrenome[idx]) for idx in range(lista_nome)]