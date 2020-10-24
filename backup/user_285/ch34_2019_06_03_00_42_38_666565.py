deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))
mês = 1
saldo = deposito
while mês <= 24:
    saldo += (saldo * (1+taxa))
    print(saldo)
    mês = mês + 1
print(saldo-deposito)