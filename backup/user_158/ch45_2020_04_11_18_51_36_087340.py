num = int(input('escreva um numero'))
lista=[]
while num != 0 and num > 0:
    lista.append(num)
    num = int(input('escreva um numero'))
lista.reverse()
print(lista)