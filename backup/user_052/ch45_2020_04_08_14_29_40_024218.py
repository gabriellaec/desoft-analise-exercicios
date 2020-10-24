lista = []
j = True
while j:
    pergunta = int(input("Digite números inteiros positivos: "))
    if pergunta > 0:
        lista.append(pergunta)
    else:
        break
i = len(lista)
while i >= 0:
    print (lista[i])
    i -= 0 