#usando for
numero = 0

for contador in range (100):
    numero = numero + (1/2**contador)
print(numero)

#usando while
contador = 0
numero = 0
 
while contador < 99:
    numero = numero + (1/2**contador)
    contador = contador + 1
print(numero)