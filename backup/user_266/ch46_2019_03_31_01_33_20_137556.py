lista=[]
i=0
while i==len(lista):
    palavra=str(input('Palavra: '))
    if palavra!='fim':
        lista.append(palavra)
    else:
        break
    i+=1
i=0
while i<len(lista):
    if lista[i][0]!='a':
        lista.remove(lista[i])
    else:
        print(lista[i])
    i+=1