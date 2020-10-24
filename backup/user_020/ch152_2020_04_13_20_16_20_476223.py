def verifica_preco(nome, livros, cores):
    nome = input("Insira o nome do livro: ")
    livros = {}
    cores = {}
    if nome in livros:
        nome = livros[nome]
        print('{0}' .format(cores))
    else:
        print("O livro {0} não existe!" .format(nome))
              