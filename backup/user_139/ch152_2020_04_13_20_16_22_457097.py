def verifica_preco(nome, cor, preco):
    lista_livros = []
    dic_livros = {}
    dic_cores = {}
    for nome in lista:
        if not nome in dic_livros:
            dic_livros [nome] = cor
        else:
            dic_livros = {}
    for cor in lista:
        if not cor in dic_cores:
            dic_cores[cor] = preco
        elif cor in dic_cores:
            dic_cores = {}
        else:
            for preco in dic_cores.values():
                return preco