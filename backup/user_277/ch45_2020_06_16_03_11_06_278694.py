lista = []
i=True
a = 1
while i:
    if a>0:
        a = int(input("digite um numero: "))
        lista.append(a)
    else:
        i=False
k=True
f=len(lista)
while k:
    print(lista[f])
    f-=1
    if f==0:
        k=False