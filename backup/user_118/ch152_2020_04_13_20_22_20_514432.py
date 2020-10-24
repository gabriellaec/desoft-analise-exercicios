def verifica_preco(livro,cores):
    dicionário_de_livros= {"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}
    cores= {"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }
    livro=input('Nome do livro: ')
    if livro in dicionário_de_livros:
        return dicionário_de_livros
    if dicionário_de_livros in cores:
        return cores