lista=[]
lista_reversa=[]
a=int(input('digite um numero:'))
i=(-1)
while a>0:
    lista.append(a)
    i+=1
    a=int(input('digite um numero:'))
while i>=0:
    lista_reversa.append(lista[i])
    i-=1
print(lista_reversa)