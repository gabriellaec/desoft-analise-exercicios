with open('churras.txt', 'r') as churras:
    grelha = churras.readlines()
    qtd = 0
    preco = 0
    montante = []
    for carvao in grelha:
        picanha = carvao.split(',')
        qtd = int(picanha[1])
        preco = float(picanha[2])
        montante.append(qtd * preco)
    print(montante)
