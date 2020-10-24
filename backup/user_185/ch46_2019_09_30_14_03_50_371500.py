lista = []
palavra = str(input("Por favor, digite uma palavra :"))
while palavra != "fim":
    lista.append(palavra)
    if palavra[0] == "a":
        print(palavra)
    palavra = str(input("Por favor, digite uma palavra :"))