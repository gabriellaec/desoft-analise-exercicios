def verifica_preco(livro, cor, preco):
    cores = cor.keys()
    precos = preco.keys()
    escolha = 0
    price = 0
    for i in cores:
        if i == livro:
            escolha = cor[i]            
    for i in precos:
        if i == escolha:
            price = preco[i]
    return price