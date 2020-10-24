def verifica_preco (titulo, dicionario_de_livros, dicionario_de_precos):
    titulo = input ('Qual o livro comprado? ')
    if titulo in dicionario_de_livros:
        preco = dicionario_de_precos[dicionario_de_livros[pergunta]]
        return preco