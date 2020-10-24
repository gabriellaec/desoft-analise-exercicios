palavras=[]
palavra=input('digite a palavra')
while(palavra!='fim'):
    if(palavra[0]=='a'):
        palavras.append(palavra)
        palavra=input('digite  a palavra')
i=0
while(i<len(palavras)):
    print(palavras[i])
    i+=1
        