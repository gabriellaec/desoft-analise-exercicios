lista = []
a = (input("Digite uma palavra: ")

while a != "fim":
    indice = 0
    if a[0] == "a":
        lista[indice] = a
        indice += 1
        a = str(input("Digite uma palavra: ")
    else:
        indice += 1
        a = str(input("Digite uma palavra: ")

print(lista)
