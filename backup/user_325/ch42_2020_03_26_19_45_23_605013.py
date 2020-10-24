palavra = input("Digite sua palavra: ")
lista = []
i = 0
while palavra != "fim":
    palavra = input("Digite sua palavra: ")
    lista.append(palavra)
    if palavra[0] == "a":
        print(palavra[i])
    i += 1