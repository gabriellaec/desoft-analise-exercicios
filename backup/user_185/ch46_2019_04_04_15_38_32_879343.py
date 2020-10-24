palavra = input("Digite uma palavra: ")
index = 0
lista = []
while palavra != "fim":
    if palavra[0:0] == "a":
        lista.append(palavra)
        palavra = input("Digite uma palavra: ")
        index = index + 1
    else:
        palavra = input("Digite uma palavra: ")
        index = index + 1