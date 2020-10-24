preco_total = 0
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    for contador in conteudo:
        listas = conteudo.strip()
        lista = listas.split(',')
        preco_total += int(listas[1])*float(listas[2])
print(preco_total)