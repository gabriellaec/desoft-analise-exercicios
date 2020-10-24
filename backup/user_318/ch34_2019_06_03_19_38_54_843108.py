deposito = int(input('quanto vc investiu ?'))
juros = float(input('Qual é a taxa de juros ? '))

mes = 1
saldo = dep_inicial

while mes <= 24:
    saldo += saldo*juros
    print(saldo)
    mes += 1
    
print(saldo - dep_inicial)