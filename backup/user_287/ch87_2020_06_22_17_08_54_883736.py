preco = 0
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    for linha in conteudo:
        lista = linha.split(',')
        mult = int(lista[1])
        print(mult)
        preco_produto = float(lista[2].strip())
        print(preco_produto)
        preco += mult*preco_produto
print(preco)