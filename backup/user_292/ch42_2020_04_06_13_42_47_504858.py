lista = []
z=1
while z>0:
    a = input('escreva uma palavra:')
    if a[0]== 'a':
        lista.append(a)
    if a == 'fim':
        lista.append(a)
        z-=1
a = len(lista)
x = 0
while x<a:
    print(lista[x])
    x+=1
