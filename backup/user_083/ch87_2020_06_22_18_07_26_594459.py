preco_total = 0
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    for contador in conteudo:
        lista = contador.split(',')
        listas = lista.strip()
        preco_total += listas[1]*listas[2]
print(preco_total)