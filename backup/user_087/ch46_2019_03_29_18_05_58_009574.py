lista = []
p = input()
while p != 'fim':
    lista.append(p)
    p = input()

for e in lista:
    if e[0] == 'a':
        print (e)