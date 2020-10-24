def verifica_preco(titulo,dicionario,tabela):
    if titulo in dicionario:
        cor = dicionario[titulo]
        return tabela[cor]