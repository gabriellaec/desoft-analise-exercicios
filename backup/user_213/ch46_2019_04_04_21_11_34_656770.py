lista=[]
i=0
pergunta=input('digite uma palavra: ')
while pergunta!='fim':
    lista.append(pergunta)
    if pergunta[0]=='a':
        print (pergunta)
    i+=1
    pergunta=input('digite uma palavra: ')
