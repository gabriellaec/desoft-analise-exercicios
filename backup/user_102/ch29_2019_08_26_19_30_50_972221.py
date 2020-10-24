salario = float(input('entre com o salário'))

if salario > 1250:
    novo_salario = salario*1.10
else:
    novo_salario = salario*1.15
print('o novo salário é {0:.2f}', format(novo_salario))