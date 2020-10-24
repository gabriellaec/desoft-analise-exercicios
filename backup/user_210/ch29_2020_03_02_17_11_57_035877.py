deposito = float(input())
taxa = float(input())
juros = 0
for _ in range(24):
    juros += deposito*taxa
    deposito = deposito*(1+taxa)
    print(deposito)

print(juros)