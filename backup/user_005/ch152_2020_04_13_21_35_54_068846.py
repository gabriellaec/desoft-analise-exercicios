def verifica_preco(livro, nome, preço):
    for x in nome:
        if x == livro:
            cor = nome[x]
    for i in preço: 
        if i == cor:
            valor = preço [i]
    return valor
            