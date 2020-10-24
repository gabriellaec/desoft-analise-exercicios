salario_bruto= float(input("Qual o seu salario bruto? "))
numero_dependentes= int(input("Quantos dependentes? "))
if salario_bruto <= 1045.00:
    contribuicao_inss = salario_bruto * 7.5/100

elif salario_bruto >= 1045.01 and salario_bruto <= 2089.60:
    contribuicao_inss = salario_bruto * 9/100

elif salario_bruto >= 2089.61 and salario_bruto <= 3134.40:
    contribuicao_inss = salario_bruto * 12/100

elif salario_bruto >= 3134.41 and salario_bruto <= 6101.06:
    contribuicao_inss = salario_bruto * 14/100

elif salario_bruto > 6101.06:
    contribuicao_inss = 671.12


base_de_calculo= salario_bruto - contribuicao_inss - (numero_dependentes * 189.59)

if base_de_calculo <= 1903.98:
    aliquota = 0
    deducao = 0

elif base_de_calculo >= 1903.99 and base_de_calculo <= 2826.65:
    aliquota = 7.5/100
    deducao = 142.80

elif base_de_calculo >= 2826.66 and base_de_calculo <= 3751.05:
    aliquota = 15/100
    deducao = 354.80

elif base_de_calculo >= 3751.06 and base_de_calculo <= 4664.68:
    aliquota = 22.5/100
    deducao = 636.13

elif base_de_calculo > 4664.68:
    aliquota = 27.5/100
    deducao = 869.36

irrf = base_de_calculo * aliquota - deducao

print(irrf)