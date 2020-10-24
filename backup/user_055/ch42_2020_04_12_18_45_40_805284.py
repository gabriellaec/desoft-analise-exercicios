palavra = input('Digite uma palavra: ')
lista_palavras = []
while palavra != "fim":
    lista_palavras.append(palavra)
    palavra = input('Digite uma palavra: ')
for letra in lista_palavras:
    if letra[0] == "a":
        print(letra)