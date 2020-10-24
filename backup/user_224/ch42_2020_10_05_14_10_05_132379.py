lista_palavras = []

palavra = input('Palavra? ')

while palavra != 'fim' :
    lista_palavras.append(palavra)
    palavra = input('Outra palavra?')

i = 0 
while i < len(lista_palavras) :
    a = lista_palavras[i]
    if a[0] == 'a':
        print(lista_palavras[i])
    i = i +1
