with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    preco = 0
    for linha in linhas:
        lista = linha.split(',')
        preco += int(lista[1])*float(lista[2])
    print(preco)
