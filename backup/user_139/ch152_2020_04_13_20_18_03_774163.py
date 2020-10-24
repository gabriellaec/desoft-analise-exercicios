def verifica_preco(nome, cor, preco):
    lista_livros = []
    lista_cores = []
    dic_livros = {}
    dic_cores = {}
    for nome in lista_livros:
        if not nome in dic_livros:
            dic_livros [nome] = cor
        else:
            dic_livros = {}
    for cor in lista_cores:
        if not cor in dic_cores:
            dic_cores[cor] = preco
        elif cor in dic_cores:
            dic_cores = {}
        else:
            for preco in dic_cores.values():
                return preco