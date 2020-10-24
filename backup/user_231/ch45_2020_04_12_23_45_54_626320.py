lista=[]
lista_reversa=[]
a=int(input('digite um numero:'))
i=(0)
while a>0:
    lista.append(a)
    i+=1
    a=int(input('digite um numero:'))
del lista[i]
while i>=0:
    lista_reversa.append(lista[i])
    i-=1
print(lista_reversa)