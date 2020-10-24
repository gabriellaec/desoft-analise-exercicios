with open ('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    conteudo2 = conteudo.split(',')
    preco = 0
    for c in range(len(conteudo2)):
        conta = conteudo2[1]*conteudo2[2]
        preco += conta

print (preco)
