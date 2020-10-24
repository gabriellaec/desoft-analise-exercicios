palavras = input('Escreva palavras: ')
lista = []
while palavra != 'fim':
    lista.append(palavras)
    palavras = input('Escreva palavras: ')
for letra in lista:
    if letra[0] == 'a':
        print (letra)