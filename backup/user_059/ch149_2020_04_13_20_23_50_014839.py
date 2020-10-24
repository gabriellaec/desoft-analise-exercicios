salario = float(input('Qual o salário bruto? '))
dependentes = int(input('Quantos dependentes? '))

base_de_calculo = 0

if salario <=1045.00:
    base_de_calculo = (salario-(salario*0.075)-(dependentes*189.59))
elif 1045.01 <= salario <= 2089.60:
    base_de_calculo = (salario-(salario*0.09)-(dependentes*189.59))
elif 2089.61 <= salario <= 3134.40:
    base_de_calculo = (salario-(salario*0.12)-(dependentes*189.59))
elif 3134.41 <= salario <= 6101.06:
    base_de_calculo = (salario-(salario*0.14)-(dependentes*189.59))
else:
    base_de_calculo = (salario-671.12)-(dependentes*189.59)
    
irrf = 0
if base_de_calculo <=1903.98:
    irrf = (base_de_calculo*0-0)
elif 1903.99 <= base_de_calculo <= 2826.65:
    irrf = (base_de_calculo*0.075)-(142.80)
elif 2826.66 <= base_de_calculo <= 3751.06:
    irrf = (base_de_calculo*0.15)-(354.80)
elif 3751.06 <= base_de_calculo <= 4664.68:
    irrf = (base_de_calculo*0.225)-(636.13)
else:
    irrf = (base_de_calculo*0.275)-(869.36)

print(irrf)