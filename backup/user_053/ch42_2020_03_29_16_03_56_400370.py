lista = []

palavra_1 = input('Digite uma palavra: ')

while palavra_1 != 'fim':
    lista.append(palavra_1)
    palavra_1 = input('Digite outra palavra: ')

i=0
while i < len(lista):
    palavra_2 = lista[i]
    if palavra_2[0] == 'a':
        print(palavra_2)
        i += 1
    else:
        i += 1