pergunta = True
lista = []
while pergunta == True:
    palavra = str(input('Digite uma palavra: '))
    lista.append(palavra)
    if palavra == 'fim':
        pergunta = False
primeira_letra = palavra[0]
if primeira_letra == 'a':
    print(palavra)