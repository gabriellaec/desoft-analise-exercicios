def verifica_preco (pergunta):
    pergunta = input ('Qual o livro comprado? ')
    if pergunta in dicionario_de_livros:
        preco = tabela_de_cores[dicionario_de_livros[pergunta]]
    return preco