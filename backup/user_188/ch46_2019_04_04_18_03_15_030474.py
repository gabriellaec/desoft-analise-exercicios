eh_fim = False
lista_palavras = []
while not eh_fim:
    palavra = int(input("Por favor digite uma palavra: "))
    if palavra == "fim":
        eh_fim = True
    else:
        lista_palavras.append(palavra)

contador = 0
while contador < len(lista_palavras):
    if lista_palavras[contador][0] == "a":
        print(lista_palavras[contador])
    contador += 1