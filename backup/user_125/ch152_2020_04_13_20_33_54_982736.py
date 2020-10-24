def verifica_preco(livros,dicionario,dicionario_cor):
    if livros in dicionario:
        cor=dicionario[livros]
    if cor in dicionario_cor:
        return dicionario_cores[cor]