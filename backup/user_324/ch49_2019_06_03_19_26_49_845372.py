lista=[]
n=int(input("digite um número: "))
while n>=0:
    lista.append(n)
    int(input("digite um número: "))
print(lista[::-1])