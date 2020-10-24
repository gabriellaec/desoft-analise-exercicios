def verifica_preco(titulo, dicionario,tabela):
    if titulo in dicionario:
        tabela=dicionario[titulo]
        if tabela in dicionario:
            preco=dicionario[tabela]
            return preco