salario = input('Qual seu salario atual? ')
                          
if salario > 1250:
    salario_aumentado = salario*1,1
print('Seu salario com aumento é R${:.2f}').format(salario_aumentado)

if salario <= 1250:
    salario_aumentado = salario*1,15
print('Seu salario com aumento é R${:.2f}').format(salario_aumentado)
                          
                          