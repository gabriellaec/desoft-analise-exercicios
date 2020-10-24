#palavras_com_a = []
palavras = []
palavra = input('Digite uma palavra: ')
while palavra != 'fim':
    palavras.append(palavra)
    palavra = input('Digite uma palavra: ')
i=0
while i<len(palavras):
    if palavras[i][0] =='a' or palavras[i][0] =='A':
        print(palavras[i])
    i+=1
    
    