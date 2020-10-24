palavras = []
palavra = input('Digite uma palavra/ fim para parar: ')
while 'fim' != palavra:
    palavras.append(palavra)
    palavra = input('Digite uma palavra/ fim para parar: ')
    
i = 0
while i < len(palavras):
    letra = palavras[i]
    if letra[0] == 'a' or letra[0] == 'A':
        print(letra)
        
    i +=1