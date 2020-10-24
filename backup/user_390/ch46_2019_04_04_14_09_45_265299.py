lista=[]
pergunta= input('palavras')
while pergunta!='fim':
    lista.append(pergunta)
    pergunta=input('palavras')
i=0
while i<len(lista):
    if lista[i][0]!='a':
        del lista[i][0]
    i+=1
print(lista)

