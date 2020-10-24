palavra = input("Palavra? ")
lista_p = []
while palavra != "fim":
    palavra = input("Palavra? ")
    if palavra[0] == "a":
        lista_p.append(palavra)
for p in lista_p:
    print(p)