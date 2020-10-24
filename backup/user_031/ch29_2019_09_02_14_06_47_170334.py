salario= float(input('Digite seu salario: '))
calcula_aumento = 0.15
if salario > 1250:
    calcula_aumento = 0.10
aumento = salario * calcula_aumento
print(aumento)