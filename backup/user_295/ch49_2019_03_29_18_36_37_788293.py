lista = []

numeros = int(input("escreva algum número para armazenar na lista"))
while numeros > 0:
    lista.append(numeros)
    numeros = int(input("escreva algum número para armazenar na lista"))

i = len(lista)-1
while i >= 0:
    print(lista[i])
    i -= 1