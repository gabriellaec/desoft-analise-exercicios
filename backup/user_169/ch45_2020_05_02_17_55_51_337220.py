num=int(input('Escreva um número inteiro e positivo '))

lista=[]

while num>0:
    lista.append(num)
    num=int(input('Escreva um número inteiro e positivo '))
    if num<=0:
        break
lista.reverse()
print(lista)