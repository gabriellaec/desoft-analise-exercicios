pica = True
lista = []

while pica:
    palavra = str(input('Digite uma palavra (fim p/ terminar): '))
    
    if palavra != 'fim':
        pica = False

    else:
        if palavra[0].lower() == 'a':
            lista.append(palavra)

while i < len(lista):
    print(lista[i])
    i += 1