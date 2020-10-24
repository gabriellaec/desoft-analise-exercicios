def verifica_preco(nome,dlivros,dcor):
    if nome in dlivros:
        c=dlivros[nome]
        if c in dcor:
            preco=dcor[c]
            return preco