lista = []
i=True
a = 1
while i:
    if a>0:
        a = int(input("digite um numero: "))
        lista.append(a)
    else:
        i=False
print(lista)
f=len(lista)
lista2=[]
rod = True
while rod:
    lista2.append(lista[f-1])
    f-=1
    if f == 0:
        rod = False
print(lista2)