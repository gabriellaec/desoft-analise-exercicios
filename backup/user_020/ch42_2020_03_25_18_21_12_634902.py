lista_palavras = []

palavra = input('Palavra? ')

while palavra != 'fim':
    lista_palavras.append(palavra)
    palavra = input('Outra palavra?')

i = 0
while i < len(lista_palavras):
    if len(palavra) > 1 and palavra[0] == 'a':
        print(palavra)
    i += 1

