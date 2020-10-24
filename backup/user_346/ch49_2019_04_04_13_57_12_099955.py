lista=[]
lista2=[]
i=0
a=int(input())
while a >0:
    lista.append(a)
    a=int(input())
while i<len(lista):
    print(lista[len(lista)-i-1])
    i+=1

    