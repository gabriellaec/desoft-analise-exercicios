lista = []
i=True
a = 1
while i:
    if a>0:
        lista.append(a)
        a = int(input("digite um numero: "))
    else:
        i=False
print(lista)
k=True
f=len(lista)
while k:
    print(lista[f-1])
    f-=1
    if f==0:
        k=False
        