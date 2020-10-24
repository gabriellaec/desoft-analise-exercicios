def verifica_preco(livro,l,p):
    if livro in l:
        procura=l[livro]
        proc=procura[1]
        if proc in p:
            preco=p[proc]
            return preco[1]