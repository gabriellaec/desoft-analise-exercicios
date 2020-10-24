fim = False
lista = []
i = 0

while not fim:
    palavra = input("Mande palavras:")

    if palavra == "fim":
        fim = True
    else:
        lista.append(palavra)

while i < len(lista):

    if lista[i][0] == "a":
        print(lista[i])
        i += 1
    else:
        i += 1