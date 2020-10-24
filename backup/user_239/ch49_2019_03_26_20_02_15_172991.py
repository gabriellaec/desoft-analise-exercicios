a=int(input('Digite um número inteiro:'))
lista=[]
while a>0:
    lista.append (a)
    a=int(input('Digite um número inteiro:'))
print(lista[::-1])