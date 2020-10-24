perg1 = float(input('Qual o seu salário bruto? '))
perg2 = int(input('Quantos são seus dependentes? '))

inss = 0
base_de_calculo = 0
irrf = 0

if perg1 <= 1045.00:
    inss = perg1*0.075
elif perg1>= 1045.01 and perg1 <= 2089.60:
    inss = perg1*0.09
elif perg1 >= 2089.61 and perg1 <= 3134.40:
    inss = perg1*0.12
elif perg1 >= 3134.41 and perg1 <= 6101.06:
    inss = perg1*0.14
else:
    inss = 671.12

base_de_calculo = perg1 - inss - perg2*189.59

if base_de_calculo <= 1903.98:
    irrf = base_de_calculo
elif base_de_calculo >= 1903.99 and base_de_calculo <= 2826.65:
    irrf = base_de_calculo*0.075 - 142.80
elif base_de_calculo >= 2826.66 and base_de_calculo <= 3751.05:
    irrf = base_de_calculo*0.15 - 354.80
elif base_de_calculo >= 3751.06 and base_de_calculo <= 4664.68:
    irrf = base_de_calculo*0.225 - 636.13
else:
    irrf = base_de_calculo*0.275 - 869.36

print('O seu IRRF é: {0}'.format(irrf))