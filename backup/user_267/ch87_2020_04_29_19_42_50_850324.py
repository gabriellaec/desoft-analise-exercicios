with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    preco = 0
    for linha in linhas:
        lista = linha.split(',')
        preco += lista[i+1]*lista[i+2]
    print(preco)