lista = []
while True:
    a = input()
    if a == 'fim':
        break
    lista.append(a)
for i in lista:
    if i[0] == 'a':
        print(i)
