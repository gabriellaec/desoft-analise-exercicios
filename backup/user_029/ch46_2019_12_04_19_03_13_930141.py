lista = []
a=input('digite uma palavra: ')
while a != 'fim':
    a=input('digite uma palavra: ')
    lista.append(a)
for i in range(len(lista)):
    if i[0]=='a':
        print(i)
