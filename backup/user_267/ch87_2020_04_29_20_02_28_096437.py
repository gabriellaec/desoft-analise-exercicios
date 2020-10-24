with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    preco = 0
    for linha in linhas:
        lista = linha.split(',')
        preco += lista[1]*lista[2]
    print(preco)
