lista = []
a = int(input("Digite um numero!"))
while a > 0:
    lista.append(a)
    a = int(input("Digite um numero!"))
    lista.reverse()
print (lista)
