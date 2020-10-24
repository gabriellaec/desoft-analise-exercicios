palavra = input("Digite sua palavra: ")
lista = []
i = 0
while palavra != "fim":
    palavra = input("Digite sua palavra: ")
    if palavra[i] == "a":
        lista.append(palavra[i])
    i += 1