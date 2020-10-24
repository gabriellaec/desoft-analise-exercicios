with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    lista = conteudo.split(',')
    preco = 0
    for i in range(len(lista)):
        preco += lista[i+1]*lista[i+2]
    print(preco)