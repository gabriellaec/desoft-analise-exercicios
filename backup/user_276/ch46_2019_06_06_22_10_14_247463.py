palavras = input('Palavras: ')
if palavras != 'fim':
lista = [palavras]
i = 0
while i < len(lista):
    while palavras != 'fim':
        palavras = input('Palavras')
        lista.append(palavras)
    i += 1    
    print(lista)