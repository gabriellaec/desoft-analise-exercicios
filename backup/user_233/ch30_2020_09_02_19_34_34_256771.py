deposito_inicial = float(input())
deposito_mensal = float(input())
juros = float(input())

saldo = deposito_inicial

for mes in range(1, 25):
    
    saldo += saldo * juros + deposito_mensal
    print("%.2f" % saldo)
    
print("%.2f" % (saldo - deposito_inicial - deposito_mensal * 24))