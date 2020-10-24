numero = int(input())
list = []

while numero > 0:
    list.append(numero)
    numero = int(input()) 

print(list[::-1])