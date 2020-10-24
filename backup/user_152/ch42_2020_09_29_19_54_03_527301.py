palavras = []
palavra = input("Entre com uma palavra: ")
while palavra != "fim":
    if palavra[0] == "a":
        palavras.append(palavra)
    palavra = input("Entre com uma palavra: ")
print(palavras)
