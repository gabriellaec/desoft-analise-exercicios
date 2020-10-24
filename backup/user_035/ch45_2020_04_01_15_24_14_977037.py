contador = True
while contador:
    pergunta = int(input("Diga números inteiros: "))
    if pergunta>0:
    lista = [1]
    lista.append(pergunta)
    else:
        contador = False
lista.reverse()
print(lista)