deposito = int(input('quanto vc investiu ?'))
juros = float(input('Qual é a taxa de juros ? '))

mes = 1
saldo = deposito

while mes <= 24:
    saldo += saldo*juros
    print(saldo)
    mes += 1
    
print(saldo - deposito)