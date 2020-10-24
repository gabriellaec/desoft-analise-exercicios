numero = True
soma = 0
while numero:
    escolhe_numero = int(input('Digite um número: '))
    if escolhe_numero != 0:
        soma = soma + escolhe_numero
    else:
        numero = False
print('A soma é {0}'.format(soma))