lista_palavras = []

palavra = input("Palavra: ")

i=0

while palavra != "fim":
    palavra = input("Palavra: ")
    if palavra[i] == 'a':
        lista_palavras.append(palavra)