deposito= float(input("Depósito: "))
deposito_inicial=deposito
taxa= float(input("Taxa de Juros: "))
ganho=0
for i in range(24):
    print(deposito*(1+taxa))
    deposito*=(1+taxa)
    ganho+=deposito*taxa
    ganho=deposito-deposito_inicial
print(ganho)

