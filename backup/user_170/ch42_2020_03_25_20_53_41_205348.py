lista = []
i = 0
lista.append(input("Adicione uma palavra: "))
while lista[i] != 'fim':
    lista.append(input("Adicione uma palavra: "))
    i += 1

k = 0

while k < len(lista):
    primeira_letra = lista[k][0]
    if primeira_letra == 'a':
        print(lista[k])
    k += 1