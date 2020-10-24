palavras = []
palavra = input('Digite uma palavra/ fim para parar: ')

for palavra in palavras:
    if palavra != 'fim':
        palavras.append(palavra)
        palavra = input('Digite uma palavra/ fim para parar: ')
    
for i in palavras:
    palavra = palavras[i]
    if palavra[0] == 'a' or palavra[0] == 'A':
        print(palavra)