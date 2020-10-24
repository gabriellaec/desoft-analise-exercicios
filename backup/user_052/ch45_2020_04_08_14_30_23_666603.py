lista = []
j = True
while j:
    pergunta = int(input("Digite números inteiros positivos: "))
    if pergunta <= 0:
        break
    else:
        lista.append(pergunta)
        
i = len(lista)
while i >= 0:
    print (lista[i])
    i -= 0 