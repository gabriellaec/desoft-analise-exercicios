def verifica_precos(titulo_cor,titulo_preco,livro):
    if livro in titulo_cor:
        cor = titulo_cor[livro]
        return ('O preço do livro é R${0:.2f}.'.format(titulo_preco[cor]))