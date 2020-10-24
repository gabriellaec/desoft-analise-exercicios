deposito = float(input())
taxa = float(input())
for _ in range(24):
    deposito = deposito*(1+taxa)
    print(deposito)
