def verifica_preco(livro,cores,precos):
    for nome,cor in cores.items():
        if nome==livro:
            cordolivro=cor
            for cor,preco in precos.items():
                if cor==cordolivro:
                    return preco