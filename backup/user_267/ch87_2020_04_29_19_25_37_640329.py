with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    preco = 0
    for i in range(len(lista)):
        lista = conteudo.split(',')
        preco += lista[i+1]*lista[i+2]
    print(preco)