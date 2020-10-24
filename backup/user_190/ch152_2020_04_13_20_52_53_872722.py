def verifica_preco(titulo, dicionario,tabela):
    if titulo in dicionario:
        cor=dicionario[titulo]
        if cor in tabela:
            preco=tabela[cor]
            return preco