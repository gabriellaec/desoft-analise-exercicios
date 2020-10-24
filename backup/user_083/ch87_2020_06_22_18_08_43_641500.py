preco_total = 0
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    for contador in conteudo:
        listas = lista.strip()
        lista = contador.split(',')
        preco_total += listas[1]*listas[2]
print(preco_total)