with open('estoque.json', 'r') as estoque:
    itens = estoque.read()
valor = 0
for i in produtos:
    valor+=i[quantidade]*i[valor]
print(valor)