salario_bruto = float(input("Digite o seu sálario bruto "))
numero_dependentes = int(input('digite o número de seus dependentes '))
print(salario_buto, numero_dependentes)
valor_de_cada_dependente = 189.59
if salario_bruto <= 1045:
    INSS = salario_bruto * 0.07,5
elif 1045.01 <= salario_bruto <= 2089.6:
    INSS = salario_bruto * 0.09
elif 2089.61 <= salario_bruto <= 3134.40:
    INSS = salario_bruto * 0.12
elif 3134.41 <= salario_bruto <= 6101.06:
    INSS = salario_bruto * 0.14
else:
    INSS = 671.12

base_de_calculo = (salario_bruto - INSS) - (numero_dependentes * valor_de_cada_dependente)

if base_de_calculo <= 1903.98:
    aliquota = 0
    deducao = 0
    IRRF = base_de_calculo * aliquota - deducao
elif 1903.99 <= base_de_calculo <= 2826.65:
    aliquota = 0.075
    deducao = 142.80
    IRRF = base_de_calculo * aliquota - deducao
elif 2826.66 <= base_de_calculo <= 3751.05:
    aliquota = 0.15
    deducao = 354.80
    IRRF = base_de_calculo * aliquota - deducao
elif 3751.06 <= base_de_calculo <= 4664.68:
    aliquota = 0.225
    deducao = 636.13
    IRRF = base_de_calculo * aliquota - deducao
else:
    aliquota = 0.275
    deducao = 869.36
    IRRF = base_de_calculo * aliquota - deducao

print('Seu imposto de renda simplificado é: {}'.format(IRRF))

