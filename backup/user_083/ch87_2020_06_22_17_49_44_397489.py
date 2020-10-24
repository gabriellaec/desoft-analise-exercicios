preco_total = 0
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    for contador in conteudo:
        lista = contador.split(',')
        quantidade = int(lista[1])
        preco = float(lista[2].strip())
        preco_total += quantidade*preco
print(preco_total)