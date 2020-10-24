digito = True
soma = 0
while digito: 
    numero = int(input ('Digite um número: '))
    if numero == 0:
        digito = False
    else:
        soma += numero

print(soma)