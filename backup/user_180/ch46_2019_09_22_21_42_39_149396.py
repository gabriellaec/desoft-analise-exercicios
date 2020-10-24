lista_palavras = []
while True:
    palavras = input("Me fale palavras: ")
    if palavras == "fim":
        break
    else:
        lista_palavras.append(palavras)
        continue
for palavra in lista_palavras:
    if palavra[0] == "a" or palavra[0] == "A":
        print(palavra)
    else:
        continue