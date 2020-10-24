lista=[]
x=0
lista.append(input('Digite uma palavra: ')
while lista[x] != 'fim':
    x +=1
    lista.append(input('Digite outra palavra: ')
n = len(lista)
i = 0
while 1 < n:
    if lista[i][0] == 'a':
        print(lista[i])
        i += 1
    else:
        i +=1