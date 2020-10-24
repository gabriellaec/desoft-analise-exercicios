'''Esse funcao serve para encontrar o valor de em livro catalogado em dois dicionarios,
o de livros e o de cor dos livros. Os livros catalogados no dicionario de livros possuem
uma cor correspondente em outro dicionario e cada cor possui o valor correspondente do
livro escolhido.
Então, a pessoa escreve o nome do livro, verifica se ele está catalogado, caso esteja,
verifica qual a sua cor corresnpondente e entao encontra o valor e retorna para o usuario
'''
def verifica_preco(nome_do_livro,catalogo_livros,catalogo_cor):
    if nome_do_livro in catalogo_livros:
        cor_do_livro = catalogo_livros[nome_do_livro]
        if cor_do_livro in catalogo_cor:
            preco_do_livro = catalogo_cor[cor_do_livro]
            return preco_do_livro