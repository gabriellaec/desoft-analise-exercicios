#palavras_com_a = []
palavras = []
palavra = input('Digite uma palavra: ')
while palavra != 'fim':
    palavras.append(palavra)
    palavra = input('Digite uma palavra: ')
i=0
while i<len(palavras):
    palavra2 = palavras[i]
    if palavra2[0] =='a' or palavra2[0] =='A':
        print(palavra2)
    i+=1
    
    