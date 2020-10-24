x = ''
lista = []
while x != 'fim':
    x = input('digite uma palavra: ')
    lista.append(x)
for palavra in lista:
    if palavra[0] == 'a':
        print(palavra)
    