livros = {"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}
cores = {"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }
def verifica_preco(nome):
    nome = input("Insira o nome do livro: ")
    if nome in livros:
        nome = livros[nome]
        print('{0}' .format(cores))
    else:
        print("O livro {0} não existe!" .format(nome))
              