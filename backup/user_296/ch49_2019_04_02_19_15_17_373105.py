a = int(input("coloque um número"))
lista = []
while a != 0:
    lista.append(a)
    a = int(input("coloque um número"))
print(lista[::-1])
    