with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

preco = 0
for linha in linhas:
    linha_concerto=linha[:2]
    itens=linha_concerto.split(',')
    print(itens)
    preco += (float(itens[1])+float(itens[2]))
    
print(preco)