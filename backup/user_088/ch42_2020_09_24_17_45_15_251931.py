palavras=[]
palavra=input('digite a palavra')
while(palavra!='fim'):
    if(palavra[0]=='a'):
        palavra.append(palavra)
        palavra=input('digite  a palavra')
print(palavras)