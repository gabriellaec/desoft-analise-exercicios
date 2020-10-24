palavra = input("Digite uma palavra: ")
lista = []
while palavra != "fim":
    if palavra[0] == "a":
        lista.append(palavra)
        palavra = input("Digite uma palavra: ")
    else:
        palavra = input("Digite uma palavra: ")
print(lista)