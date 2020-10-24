lista_palavras = []

usuario = input("Palavra")
lista_palavras.append(usuario)

while(usuario != "fim"):
    usuario = input("outra palavra ")
    lista_palavras.append(usuario)
    
i = 0

while (i < len(lista_palavras)):
    x = lista_palavras[i]
    if (x[0] == 'a'):
        print (x)
    i += 1