#definindo a funcao 
def verifica_preco(titulo_livro,dicionário_de_livros,tabela_de_cores):
    if titulo_livro in dicionário_de_livros:
        cor = dicionário_de_livros[titulo_livro]
    if cor in tabela_de_cores:
        preco = tabela_de_cores[cor]
        return preco 