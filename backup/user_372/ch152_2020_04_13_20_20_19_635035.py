def verifica_preco(dic1,dic2,nome):
    dic1={}
    dic2={}
    nome=str(input('Qual o título do livro que você deseja consultar o preço? '))
    while nome in dic1.keys():
        cor=dic1['nome']
        if cor in dic2.keys():
            preco=dic2[preco]
            return preco