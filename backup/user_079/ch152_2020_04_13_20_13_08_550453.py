def verifica_preco(nome, livro, cor):
    for k,v in livro.items():
        if k == nome:
            for x,y in cor.items():
                if x == v:
                    return y