lista=[]
x=0
lista.append(input('Digite uma palavra: '))
while lista[x] != 'fim':
    x +=1
    lista.append(input('Digite outra palavra: '))

for palavra in lista:
    if palavra[0] == 'a':
        print(palavra)
    