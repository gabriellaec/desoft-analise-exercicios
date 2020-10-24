s=0
p=1
lista = []
while p>=1/2**99:
    lista.append(p)
    p=p/2
for i in lista:
    s += i
print(s)