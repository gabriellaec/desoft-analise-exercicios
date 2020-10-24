digito = True

while digito: 
    numero = int(input ('Digite um número: '))
    if numero == 0:
        digito = False
    else:
        numero += numero
        
print(numero)