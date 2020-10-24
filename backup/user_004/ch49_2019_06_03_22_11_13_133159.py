lista=[]
num=int(input('Digite um número: '))
lista.append(num)
while num > 0:
    num=float(input('Digite outro número: '))
    if num>0:
        lista.append(num)

lista1 = lista.reverse()
print(lista)