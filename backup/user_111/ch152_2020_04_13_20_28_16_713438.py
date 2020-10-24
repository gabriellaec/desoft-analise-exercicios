def verifica_preco(livro,livros,cores):
    livro=input("Digite o nome do livro: ")
    dic_de_livros={}
    tabela_de_cores: {"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }
    precos=tabela_de_cores
    for i in range(len(livros)):
        dic_de_livros[livros[i]]=cores[i]
    for j in range(len(cores)):
        tabela_de_cores[cores[i]]=precos[i]
    x=tabela_de_cores[dic_de_livros[livro]]
    return x