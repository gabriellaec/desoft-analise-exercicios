def verifica_preco (livros, precos):
    livros={"TdeV" : "roxo", "HP" : "vermelho", "SW" : "azul", "PJ": "verde"}
    precos={"roxo": 50.00, "vermelho" : 45.00, "azul" : 48.00, "verde" : 27.00}
    cor=livros[livro]
    preco=precos[cor]
    print ('{0} custa {1}'.format(livro, preco))
        