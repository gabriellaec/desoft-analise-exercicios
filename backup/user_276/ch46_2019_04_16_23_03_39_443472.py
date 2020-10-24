palavras = input('Palavras')
lista = [palavras]
i = 0
while i < len(lista):
    while palavras != 'fim':
        palavras = input('Palavras')
        lista.append(palavras)
    i += 1    
    print(lista)