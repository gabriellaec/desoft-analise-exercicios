preco = 0
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    for linha in conteudo:
        lista = linha.split(',')
        mult = int(lista[1])
        print(mult)
        produto = float(lista[2].strip())
        print(produto)
        preco += mult*produto
print(preco)