lista=[]
x=0
lista.append(input('manda ai: '))
while lista[x]!= 'fim':
    x+=1
    lista.append(input('manda ai: '))
tamanho=len(lista)
i=0
while i<tamanho:
    if lista[i][0]=='a':
        print (lista[i])
        i+=1
    else:
        i+=1
