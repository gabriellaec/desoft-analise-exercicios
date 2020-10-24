def verifica_preco(nome,dicionario,tabela):
    cor = 0
    if nome in dicionario:
        cor = dicionario[nome]
    
    if cor in tabela:
        return tabela[cor]