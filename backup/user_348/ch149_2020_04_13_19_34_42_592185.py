salario_bruto = float(input('Qual o salario bruto?: '))
dependentes = int(input('Digite o numero de dependentes: '))

if salario_bruto <= 1045.00:
    base_calculo = salario_bruto - salario_bruto*0.075 - dependentes*189.59
elif salario_bruto >= 1045.01 and salario_bruto <= 2089.60:
    base_calculo = salario_bruto - salario_bruto*0.09 - dependentes*189.59
elif salario_bruto >=  2089.61 and salario_bruto <= 3134.40:
    base_calculo = salario_bruto - salario_bruto*0.12 - dependentes*189.59
elif salario_bruto >= 3134.41 and salario_bruto <= 6101.06:
    base_calculo = salario_bruto - salario_bruto*0.14 - dependentes*189.59
elif salario_bruto > 6101.06:
    base_calculo = salario_bruto - 671.12 - dependentes*189.59

IRRF = base_calculo*aliquota - dedução
if base_calculo <= 1903.98:
    IRFF = base_calculo*0 - 0
elif base_calculo >= 1903.99 and base_calculo <=  2826.65:
    IRFF = base_calculo*0.075 - 142.80
elif base_calculo >= 2826.66 and base_calculo <= 3751.05:
    IRFF = base_calculo*0.15 - 354.80
elif base_calculo >= 3751.06 and base_calculo <= 4664.68:
    IRFF = base_calculo*0.225 - 636.13
elif base_calculo > 4664.68:
    IRFF = base_calculo*0.275 - 869.36
    
print(IRRF)







