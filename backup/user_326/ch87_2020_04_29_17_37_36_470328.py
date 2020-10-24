preco_total = 0
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    print(conteudo)
    for linha in conteudo:
        lista = linha.split(',')
        print(lista)
        multiplicador = lista[1]
        preco_produto = lista[2]
        preco_total += multiplicador*preco_produto
print(preco_total)