salario_bruto = float(input())
numero_de_dependentes = int(input())

# INSS

if salario_bruto <= 1045.00:
    contribuicao_para_o_INSS = 0.075 * salario_bruto
elif 1045.01 <= salario_bruto <= 2089.60:
    contribuicao_para_o_INSS = 0.09 * salario_bruto
elif 2089.61 <= salario_bruto <= 3134.40:
    contribuicao_para_o_INSS = 0.12 * salario_bruto
elif 3134.41 <= salario_bruto <= 6101.06:
    contribuicao_para_o_INSS = 0.14 * salario_bruto
elif salario_bruto >= 6101.07:
    contribuicao_para_o_INSS = 671.12

base_de_calculo = salario_bruto - contribuicao_para_o_INSS - numero_de_dependentes * 189.59

# ALIQUOTA E DEDUCAO

if base_de_calculo <= 1903.98:
    aliquota = 0
    deducao = 0
elif 1903.99 <= base_de_calculo <= 2826.65:
    aliquota = 0.075
    deducao = 142.80
elif 2826.66 <= base_de_calculo <= 3751.05:
    aliquota = 0.15
    deducao = 354.80
elif 3751.05 <= base_de_calculo <= 4664.68:
    aliquota = 0.225
    deducao = 636.13
elif base_de_calculo >= 4664.69:
    aliquota = 0.275
    deducao = 869.36

IRRF = base_de_calculo * aliquota - deducao