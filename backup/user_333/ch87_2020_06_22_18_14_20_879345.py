with open('cancao_do_exilio.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

preco = 0
for linha in linhas:
    itens=linha.split(',')
    preco += (itens[1]+itens[2])
    
print(preco)