def verifica_preco (string, dic_livros, dic_cores):
    if string in dic_livros:
        for i in dic_livros:
            for o in dic_cores:
                if dic_livros[i] == o and string == i:
                    return dic_cores[o]