num = float(input("Escreva um numero: ))
lista = []
soma = 0
while num > 0:
    lista.append(num)
if num == 0:
    for i in lista:
        soma += lista[i]
print (soma)