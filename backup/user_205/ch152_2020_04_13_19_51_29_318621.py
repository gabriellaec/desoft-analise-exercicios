def verifica_preco(titulo,dicionario,cores):
    for livro,cor in dicionario.items():
        if titulo == livro:
            for cor,preco in cores.items():
                return preco
        