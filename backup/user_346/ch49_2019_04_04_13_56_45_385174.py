lista=[]
lista2=[]
i=0
a=int(input())
while a >0:
    lista.append(a)
    a=int(input())
while i<len(lista):
    lista2.append(lista[len(lista)-i-1])
    