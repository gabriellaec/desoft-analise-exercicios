def verifica_precos(titulo_cor,titulo_preco):
    livro = input('Qual o livro?')
    if livro in titulo_cor:
        cor = titulo_cor[livro]
        preco = titulo_preco[cor]
        return ('O preço do livro é R${0:.2f}.'.format(preco))