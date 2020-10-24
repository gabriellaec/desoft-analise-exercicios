palavras = []
palavra = str
while True:
    palavra = input('Digite uma palavra: ')
    if palavra == 'fim':
        break
    palavras.append(palavra)
for palavra in palavras:
    if palavra[0] == 'a':
        print(palavra)