deposito = float(input())
taxa = float(input())
for _ in range(25):
    deposito = deposito*(1+taxa)
    print(deposito)
