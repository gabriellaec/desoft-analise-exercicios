deposito_inicial= float(input("Depósito: "))
deposito_final=0
taxa= float(input("Taxa de Juros: "))
ganho=0
for i in range(24):
    print(deposito_inicial*(1+taxa))
    deposito_final=deposito_incial*(1+taxa)
ganho=deposito_final- deposito_inicial
print(ganho)
