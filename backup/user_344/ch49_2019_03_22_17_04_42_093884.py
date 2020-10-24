lista=[]
num=int(input('Digite um numero: '))
while num > 0:
    lista.append(num)
    num=int(input('Digite um numero: '))
i=len(lista)-1
while i>=0:
    print(lista[i])
    i-=1