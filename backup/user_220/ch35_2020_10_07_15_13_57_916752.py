pergunta = int(input("Qual o numero? "))
lista = []
while pergunta != 0:
    lista.append(pergunta)
    pergunta = int(input("Qual o numero? "))
print(sum(lista))

