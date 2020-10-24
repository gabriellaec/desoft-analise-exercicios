a=1
numeros=[]
while a>0:
    a=int(input('digie um número'))
    if a>0:
        numeros.append(a)
b=len(numeros)-1
while b>=0:
    print(numeros[b])
    b-=1

    