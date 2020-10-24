lista=[]
pergunta= input('palavras')
while pergunta!='fim':
    lista.append(pergunta)
    pergunta=input('palavras')
i=0
while i<len(lista):
    if lista[i][0]=='a':
        print (lista[i])
        i+=1
    else:
        i+=1
    
