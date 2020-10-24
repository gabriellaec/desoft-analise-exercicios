dep_inicial = int(input('Valor depositado ?'))
juros = float(input('Qual o juros? '))

mes = 1
saldo = dep_inicial

while mes <= 24:
    saldo += saldo*juros
    print(saldo)
    mes += 1
    
print(saldo - dep_inicial)
    