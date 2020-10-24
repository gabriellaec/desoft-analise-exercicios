with open('churras.txt', 'r') as churras:
    grelha = churras.readlines()
    qtd = 0
    preco = 0
    for picanha in grelha:
        picanha.replace("''", '')
        alcatra = picanha.split(',')
        for pao_de_alho in alcatra[1]:
            qtd += pao_de_alho
        for fritas in alcatra[2]:
            preco += fritas
    montante = qtd * preco
    print(montante)