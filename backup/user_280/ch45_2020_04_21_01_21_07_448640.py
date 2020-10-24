numero = int(input('Digite um numero: '))
lista = []
while numero > 0:
    lista.append(numero)
    numero = int(input('Digite um numero: '))

lista2 = []
i=0
while i < len(lista):
    lista2.append(lista[len(lista) - i])
    i+=1
    
print(lista2)