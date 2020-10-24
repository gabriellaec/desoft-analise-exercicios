def verifica_preço(titulo, livro, cor):
    tit2liv = {}
    liv2cor = {}
    cor2pr = {}
    
    for titulo in tit2liv.keys():
        livro = tit2liv[titulo]
        for livro in liv2cor.keys():
            cor = liv2cor[livro]
            for cor in cor2pr.keys():
                pr = cor2pr[cor]
                return pr
    