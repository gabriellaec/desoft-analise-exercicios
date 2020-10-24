lista = [0]*5

lista[0] = input('Digite uma palavra: ')
lista[1] = input('Digite uma palavra: ')
lista[2] = input('Digite uma palavra: ')
lista[3] = input('Digite uma palavra: ')
lista[4] = 'fim'

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