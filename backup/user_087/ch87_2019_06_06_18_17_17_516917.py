with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()

for linha in conteudo:
    lista = list(linha.split(','))
    
quantidade = lista[1]
valor = lista[2]

print(quantidade*valor)
        