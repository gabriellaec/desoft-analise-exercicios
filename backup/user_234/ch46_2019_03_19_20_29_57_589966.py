lista_palavras = []

palavra = input("Palavra: ")

i=0

while palavra != "fim":
    if palavra[i] == 'a':
        lista_palavras.append(palavra)
    palavra = input("Palavra: ")

num_lista = len(lista_palavras)
n=0
while n < num_lista:
    print(lista_palavras[n])
    n+=1