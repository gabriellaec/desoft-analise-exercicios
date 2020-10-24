lista=[]
resposta=input('Palavra: ')
lista.append(resposta)
x=0
while lista[x]!='fim':
    x+=1
    resposta=input('Palavra: ')
i=0
while i<len(lista):
    if lista[0]=='a':
        print(lista[i])
        i+=1

    