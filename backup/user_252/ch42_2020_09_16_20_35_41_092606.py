lista=[]
resposta=input('Palavra: ')
lista.append(resposta)

while lista[-1]!='fim':
    resposta=input('Palavra: ')
    lista.append(resposta)
i=0
while i<len(lista):
    if lista[i][0]=='a':
        print(lista[i])
    i+=1

    