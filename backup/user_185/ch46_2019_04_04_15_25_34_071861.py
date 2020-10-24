palavra = input("Digite uma palavra")
index = 0
lista = []
while index <= len(lista):
    if palavra != "fim":
        lista.append(palavra)
        palavra = input("Digite uma palavra")
        index = index + 1
    else:
        break
print(lista)