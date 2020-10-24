palavra = input("Digite palavra: ")
lista = []
i = 0
while palavra != "fim":
    palavra = input("Digite palavra: ")
    lista.append(palavra)
    if palavra[0] == "a":
        print(palavra)
    i += 1