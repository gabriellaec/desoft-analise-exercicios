def verifica_preco(titulo,titulo_cor,cor_preco):
    cor=titulo_cor[titulo]  #transforma o titulo do livro em sua cor de referência
    preco=cor_preco[cor]  #transforma a cor no preço do livro escolhido
    return preco