
lista = []
j = True
while j:
    pergunta = int(input("Digite números inteiros positivos: "))
    if pergunta > 0:
        lista.append(pergunta)
        print (lista)
    else:
        x = len(lista)
        while x > i:
            x -=1
            print (lista[x])