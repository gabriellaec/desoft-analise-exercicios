palavras = []
palavra = input('digite uma palavra:')
while 'fim'!= palavra:
    palavras.append(palavra)
    palavra = input('digite uma palavra')
i = 0
while i<len(palavras):
    palavra = palavras[i]
    if palavra[0] == 'a'or palavra[0] == 'A':
        print(palavra)
    i = i + 1