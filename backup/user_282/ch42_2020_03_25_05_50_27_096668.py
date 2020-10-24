#Preenche lista ate a palavra 'fim'
lista_palavras = []

palavra = input('palavra? ')

while palavra != 'fim':
    lista_palavras.append(palavra)
    palavra = input('outra palavra ')
    
#Imprime apenas as palavras que começam com 'a'
i = 0
while i < len(lista_palavras):
    palavra = lista_palavras[i]
    if len(palavra) > 0 and palavra[0] == 'a':
        print(palavra)
    i += 1