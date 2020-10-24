pergunta_palavras=input('Digite uma palavra: ')
l=[]
while pergunta_palavras!='fim':
    pergunta_palavras=input('Digite uma palavra: ')
    l.append(pergunta_palavras)
if pergunta_palavras=='fim':
    for i in l:
        if i[0]=='a':
            print(i)
    
    