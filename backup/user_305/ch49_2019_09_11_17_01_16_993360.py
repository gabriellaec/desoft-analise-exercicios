lista = []
lista2 = []
a = input("Numeros")
while a != 0 or a>0:
    lista.append(a)
    a = input("Numeros")
for i in reversed(lista):
    lista2.append(i)
print (lista2)