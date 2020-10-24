def verifica_preco(livro,livros,cores):
    livro=input("Digite o nome do livro: ")
    precos=[]
    dic_de_livros={}
    tabela_de_cores={}
    for i in range(len(livros)):
        dic_de_livros[livros[i]]=cores[i]
    for j in range(len(cores)):
        tabela_de_cores[cores[i]]=precos[i]
    if livro in dic_de_livros:
        