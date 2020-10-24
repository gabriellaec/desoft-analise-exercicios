numero = True
while numero:
    escolhe_numero = int(input('Digite um número: ')
    soma_anterior = 0
    if escolhe_numero != 0:
       soma = soma_anterior + escolhe_numero
       soma_anterior += soma
    else:
        numero = False

print('A soma é {0}'.format(soma))