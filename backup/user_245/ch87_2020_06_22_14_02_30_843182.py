preco = 0
with open('churras.txt') as churras:
    conteudo = churras.readlines()
    for linha in conteudo:
        lista = linha.split(',')
        mult = int(lista[1])
        prod = int(lista[2])
        preco += mult*prod
print (preco)