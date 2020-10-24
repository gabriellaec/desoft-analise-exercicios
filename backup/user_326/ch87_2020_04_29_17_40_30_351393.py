preco_total = 0
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    for linha in conteudo:
        lista = linha.split(',')
        multiplicador = lista[1]
        preco_produto = float(lista[2].strip())
        print(preco_produto)
        preco_total += multiplicador*preco_produto
print(preco_total)