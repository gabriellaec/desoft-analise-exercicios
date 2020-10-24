lista_palavras = []

palavra = input("Palavra: ")

i=0

while palavra != "fim":
    palavra = input("Palavra: ")
    if palavra[i] == 'a':
        lista_palavras.append(palavra)

num_lista = len(lista_palavras)
n=0
while n < 0:
    print(lista_palavras[i])