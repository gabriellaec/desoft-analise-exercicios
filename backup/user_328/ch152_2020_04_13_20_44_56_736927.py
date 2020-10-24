def verifica_preco(nome,titulo,cor):
    if nome in titulo:
        x = titulo[nome]
        if x in cor:
            preco = cor[x]
            return preco
    