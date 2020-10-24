with open ('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()

lista = []
for i in conteudo:
    a = i.split(',')
    lista.append(a)

valor = 0
for c in range(len(lista)):
    nome = lista[c][0]
    qnt = int(lista[c][1])
    preco = float(lista[c][2])
    conta = qnt*preco
    valor += conta

print (valor)