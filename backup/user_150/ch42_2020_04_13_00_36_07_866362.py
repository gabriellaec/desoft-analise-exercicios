pergunta = True
lista = []
while pergunta == True:
    palavra = str(input('Digite uma palavra: '))
    lista.append(palavra)
    if palavra == 'fim':
        pergunta = False
i = 0
while i < len(lista):
    primeira_letra = palavra[0]
    if primeira_letra == 'a':
        print(lista[i])
    i += 1