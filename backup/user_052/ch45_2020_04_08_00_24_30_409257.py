
lista = []
j = True
while j:
    pergunta = int(input("Digite números inteiros positivos: "))
    if pergunta > 0:
        lista.append(pergunta)
        print (lista)
        pergunta = int(input("Quer outro valor: "))
    else:
        x = len(lista)
        while x > i:
            x -=1
            print (lista[x])