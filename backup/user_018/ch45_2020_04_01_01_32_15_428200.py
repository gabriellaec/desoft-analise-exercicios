lista = []
n = int(input('N = '))
while n > 0 or n!=0:
    lista.append(n)
    n = int(input('N = '))
print(lista[::-1])