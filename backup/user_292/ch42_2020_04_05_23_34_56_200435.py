lista = []
z=1
while z>0:
    a = input('escreva uma palavra:')
    if a[0]== 'a':
        lista.append(a)
        print(lista)
    if a == 'fim':
        lista.append(a)
        z-=1
        print(lista)
