lista = []

num = int(input('numero inteiro e positivo :'))

while num > 0:
    lista.append(num)

    num = int(input('numero inteiro e positivo :'))
    
lista = reversed(lista)