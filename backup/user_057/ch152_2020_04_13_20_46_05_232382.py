def verifica_preco(titulo, dicionario, tabela):
    if titulo in dicionario.keys():
        cor = dicionario[titulo]
    if cor in tabela.keys():
        preco = tabela[cor]
    return preco