lista = []
a = int(input('Qual o número?'))
while a > 0:
    lista.append(a)
    a = int(input('Qual o número?'))
print(lista[::-1])