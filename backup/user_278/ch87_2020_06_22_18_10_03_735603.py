with open ('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    conteudo2 = conteudo.split(',')
    preco = 0
    for c in range(len(conteudo2)):
        conta = int(conteudo2[1])*float(conteudo2[2])
        preco += conta

print (preco)
