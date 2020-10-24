numero_positivo = True
lista = []
while numero_positivo:
    pergunta = int(input('Digite números inteiros positivos: '))
    if pergunta < 0:
        numero_positivo = False
    lista.append(pergunta)
        
print(lista)
lista.reverse()
print(lista)
