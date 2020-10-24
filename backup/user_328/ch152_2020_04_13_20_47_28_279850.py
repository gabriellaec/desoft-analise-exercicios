def verifica_preco(nome,titulo,corlivro):
    if nome in titulo:
        x = titulo[nome]
        if x in corlivro:
            preco = corlivro[x]
            return preco
    