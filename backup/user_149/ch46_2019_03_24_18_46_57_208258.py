palavras=[]
palavra=input('Digite uma palavra')
while palavra != 'fim':
    palavra=input('Digite uma palavra')
    palavras.append(palavra)
    
i=0
while i<len(palavras):
    if palavras[i][0]=='a':
        print(palavras[i])
    i+=1
    