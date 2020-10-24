lista = []
lista2 = []
a = input("Numeros")
while True:
    if a != 0 and a>0:
    	lista.append(a)
    	a = input("Numeros")
    else:
        break
for x in reversed(lista):
    lista2.append(x)
print (lista2)