lista = []

while numeros != 0:
    lista.append(numeros)
    numeros = int(input("escreva algum número para armazenar na lista"))

i = len(lista)-1

lista_reversa = []

while i >= 0:
    lista_reversa.append (lista[i])
    i -= 1