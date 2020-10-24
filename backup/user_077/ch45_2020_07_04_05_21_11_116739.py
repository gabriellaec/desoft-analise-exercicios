a=0
numeros=[]
reversa=[]
while a>0:
    a=int(input('digie um número'))
    numeros.append(a)
b=len(numeros)-1
while b>=0:
    reversa.append(numeros[b])
    b-=1
for n in reversa:
    print(n)

    