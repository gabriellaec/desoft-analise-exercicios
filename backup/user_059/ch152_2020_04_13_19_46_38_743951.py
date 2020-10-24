def verifica_preco(nome, livcor, corpre):
    cor = 0
    for i in range(len(livcor)):
        if nome in livcor:
            cor = livcor[nome]
    preco = 0
    for e in range(len(corpre)):
        if cor in corpre:
            preco = corpre[cor]
    return preco
