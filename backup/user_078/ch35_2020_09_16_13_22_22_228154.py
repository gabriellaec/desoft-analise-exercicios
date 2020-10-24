pica = True
soma = 0

while pica:
    numero = float(input('Insira um número: '))
    
    if numero == 0:
        soma += 0
        print (soma)
        pica = False

    else:
        soma += numero

print(soma)