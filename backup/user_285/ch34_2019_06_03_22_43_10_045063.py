deposito= float(input("Depósito: "))
taxa= float(input("Taxa de Juros: "))
ganho=0
for i in range(24):
    deposito1=deposito
    print(deposito1*(1+taxa))
    deposito1=deposito*(1+taxa)
    ganho+=deposito*taxa
print(ganho)
