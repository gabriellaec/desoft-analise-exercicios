numero = True
while numero:
    escolhe_numero = int(input('Digite um número: ')
    i = 0
    if escolhe_numero != 0:
       soma = i + escolhe_numero
       i += soma
    else:
        numero = False

print('A soma é {0}'.format(soma))