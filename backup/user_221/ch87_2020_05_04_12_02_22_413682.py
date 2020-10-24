with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    lista = conteudo.split(',')
valor = 0
for linha in lista:
    produto = linha.split(',')
    valor += int(produto[1]) * float(produto[2])
print(valor)