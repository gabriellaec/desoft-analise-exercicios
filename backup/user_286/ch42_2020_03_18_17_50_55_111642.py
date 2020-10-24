palavra = input('Digite uma palavra: ')
lista = [palavra]
while palavra != 'fim':
    palavra = input('Digite uma palavra: ')
    if palavra != 'fim':
        lista.append(palavra)

for a in lista:
    if a[0] == 'a':
        print(a)
