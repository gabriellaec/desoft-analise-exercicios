lista=[]
a=input('Insira uma palavra')
lista.append(a)
i=0
while lista[i]!='fim':
    lista.append(input('Insira outra palavra'))
    i+=1
c=0
while lista[c][0]=='a' and c<len(lista):
    print(lista[c])
    c+=1
    

      
