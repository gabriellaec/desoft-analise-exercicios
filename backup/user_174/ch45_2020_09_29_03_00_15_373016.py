x=1
lista=[]
while int(x)>0:
    x=input("Digite um elemento da lista: ")
    lista.append(x)

n=len(lista)
b=[]
x=n-1

while len(lista)!=len(b):
    b.append(lista[x])
    lista[x]=lista[x-1]
    x=x-1

print(b)