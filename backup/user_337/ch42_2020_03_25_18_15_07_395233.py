lista = []

p = input('dig palav')

while p != 'fim':
    lista.append(p)
    p = input('outra palav')

i = 0
while i < len(lista):
    p = lista[i]
    if len(p) >= 1 and p[0] == "a":
        print(p)
    i += 1
	