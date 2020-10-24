palavra = input('Digite uma palavra: ')
lista = []
while palavra != 'fim':
    lista.append(palavra)
    palavra = str(input('Digite uma palavra: '))
for letra in lista:
    if letra[0] == 'a':
        print(letra)