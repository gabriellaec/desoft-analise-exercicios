palavras = []
palavra = input('Digite uma palavra: ')
while palavra != 'fim':
    palavras.append(palavra)
    palavra = input('Digite outra palavra: ')

#print (palavras)
i = 0
while i < len(palavras):
    palavra = palavras[i]
    if len(palavras) > 1 and palavra[0] == 'a':
        print(palavra)
    i += 1