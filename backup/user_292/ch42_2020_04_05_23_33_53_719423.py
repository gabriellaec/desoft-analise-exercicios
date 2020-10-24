lista = []
z=1
while z>0:
    a = input('escreva uma palavra:')
    if a[0]== 'a':
        lista.append(a)
    if a == 'fim':
        z-=1
print(lista)
