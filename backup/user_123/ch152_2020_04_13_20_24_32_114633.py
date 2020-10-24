def verifica_preco(titulo,dicionario,valor):
    if titulo in dicionario:
        val = dicionario[titulo]
    if val in valor:
        preco = valor[val]
    return preco