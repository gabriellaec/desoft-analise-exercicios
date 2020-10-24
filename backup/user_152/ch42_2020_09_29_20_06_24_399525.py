palavras = []
palavra = input("Entre com uma palavra: ")
while palavra != "fim":
    palavras.append(palavra)
    palavra = input("Entre com uma palavra: ")
i = 0
size = len(palavras)
while i<size:
    palavra = palavras[i]
    i += 1
    if palavra[0] == "a":
        print(palavra)
