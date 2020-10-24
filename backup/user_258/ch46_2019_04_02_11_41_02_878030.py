lista=[]
lista=input('Palavra: ')
while lista!='fim':
    lista=input('Palavra: ')
    lista.append(lista)
i=0
while i<len(lista):
    if lista[i][0]=='a':
        print(lista[i])
    i+=1

    