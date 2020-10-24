lista = [0]*6

lista[0] = input('Digite uma palavra: ')
lista[1] = input('Digite uma palavra: ')
lista[2] = input('Digite uma palavra: ')
lista[3] = input('Digite uma palavra: ')
lista[4] = input('Digite uma palavra: ')
lista[5] = input('Digite uma palavra: ')

i=0

while i < len(lista):
    palavra = lista[i]
    primeira_letra = palavra[0]

    if primeira_letra == 'a':
        print(palavra)
        i += 1
    else:
        i += 1

print('')
print('fim')