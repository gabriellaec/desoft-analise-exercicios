n=0
lista=[input('escreva uma palavra: ')]

while lista[n]!='fim':
    lista.append(input('escreva uma palavra: '))
    n+=1

i=0
while i<len(lista):
    palavra=lista[i]
    if palavra[0]!='a' or palavra[0]!='A':
        del(lista[i])
    else:
        i+=1

 j=0
while j<len(lista):
    print(lista[j])
    j+=1
    