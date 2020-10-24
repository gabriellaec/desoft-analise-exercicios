lista = []
j = True
while j:
    pergunta = int(input("Digite números inteiros positivos: "))
    if pergunta > 0:
        lista.append(pergunta)
        print (lista)
        pergunta = int(input("Quer outro valor: "))
    else:
        print (lista)