lista = []
while True:
    palavra = input("digite uma palavra: ")
    if palavra != 'fim':
        lista.append(palavra)
    else:
        break

i = 0
while i < len(lista):
    if lista[i][0] == 'a':
        print(lista[i])
    i += 1