lista=[]
numero=int(input('Digite um numero: '))
while numero > 0:
    lista.append(numero)
    numero=int(input('Digite um numero: '))
    
print(lista[::-1])