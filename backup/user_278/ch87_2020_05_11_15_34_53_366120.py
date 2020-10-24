with open ("churras.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
    
lista = []
dic = {}
for i in conteudo:
    a = i.split(",")
    lista.append(a)

soma = 0
for x in range (0,len(lista)):
    nome = lista[x][0]
    quantidade = int(lista[x][1])
    valor = float(lista[x][2])
    soma = soma + (quantidade*valor)
print (soma)