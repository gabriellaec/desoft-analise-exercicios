with open('churras.txt', 'r') as churras:
    grelha = churras.readlines()
    qtd = 0
    preco = 0
    for picanha in grelha:
        alcatra = picanha.split(',')
        qtd += int(alcatra[1])
        preco += int(alcatra[2])
    montante = qtd * preco
    print(montante)