def verifica_preco (string, dic_livros, dic_precos):
    #string é k de dic_livros
    #cor é v de dic_livros e k de dic_precos
    #preco é v de dic_precos
    if string in dic_livros:
        cor = dic_livros[string]
    if cor in dic_precos:
        preco = dic_precos[cor]
        return preco