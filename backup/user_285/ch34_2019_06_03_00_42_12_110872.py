depósito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))
mês = 1
saldo = depósito
while mês <= 24:
    saldo += (saldo * (1+taxa))
    print(saldo)
    mês = mês + 1
print(saldo-depósito)