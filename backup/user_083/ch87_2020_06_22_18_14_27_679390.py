preco_total = 0
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    for contador in conteudo:
        lista = contador.split(',')
        quantidade = listas[1]
        preco = listas[2]
        preco_total += int(quantidade)*float(preco)
print(preco_total)