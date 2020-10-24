a = int(input('Digite um número '))
lista = []
while a > 0:
    lista.append(a)
    a = int(input('Digite um número '))

lista2 = []
i = len(lista) - 1
#x = 0
while i >= 0:
    lista2.append(lista[i])
    i = i - 1
    #x +=1

#x = x - 1
#del lista2[x]
print(lista2)