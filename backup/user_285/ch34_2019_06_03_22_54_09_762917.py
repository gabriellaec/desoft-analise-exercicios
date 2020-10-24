deposito= float(input("Depósito: "))
taxa= float(input("Taxa de Juros: "))
ganho=0
for i in range(24):
    print(deposito*(1+taxa))
    deposito*=(1+taxa)
    ganho+=deposito-(deposito*taxa)
print(ganho)
