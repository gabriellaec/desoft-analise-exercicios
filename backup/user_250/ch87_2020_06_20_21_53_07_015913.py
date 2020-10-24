with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
tot = 0
    for i in linhas:
        lista = i.split(',')
        qte = lista[1]
        preco = lista[2]
        tot += preco*qte
print(tot)
        
    