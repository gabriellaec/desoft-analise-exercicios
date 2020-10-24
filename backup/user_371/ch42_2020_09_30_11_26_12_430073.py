lista=[]
i = 0
palavra = (input("Digite a palavra: "))
while palavra != "fim":
    if palavra[0] == "a":
        lista.append(palavra)
        palavra = (input("Digite a palavra: "))
    else:
        palavra = (input("Digite a palavra: "))
while len(lista) > i:
    print(lista[i])
    i += 1