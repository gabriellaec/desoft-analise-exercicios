lista_palavras = []
j = True
while j:
    palavra = input("Escolha algumas palavras: ")
    if palavra[0] == "a":
        lista_palavras.append(palavra)
        print (palavra)
    if palavra == "fim":
        j = False