preco_total = 0
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    for contador in conteudo:
        listas = contador.strip()
        lista = listas.split(',')
        preco_total += listas[1]*listas[2]
print(preco_total)