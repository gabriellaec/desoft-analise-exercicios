def verifica_preco(lista):
    dic_livros = {}
    dic_cores = {}
    for nome in lista:
        if not nome in dic_livros:
            dic_livros [nome] = []
        else:
            dic_livros = {}
    for cor in lista:
        if not cor in dic_cores:
            dic_cores[cor] = []
        elif cor in dic_cores:
            dic_cores = {}
        else:
            for preco in dic_cores.values():
                return preco