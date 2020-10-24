salario_bruto = float(input("Seu salario bruto: "))
dependentes = float(input("numero de dependentes do usuario: "))

if salario_bruto <= 1045.00:
    INSS = (salario_bruto)*0.075
elif 1045.00 < salario_bruto <= 2089.60:
    INSS = (salario_bruto)*0.09
elif 2089.60 < salario_bruto <= 3134.40:
    INSS = (salario_bruto)*0.12
elif 3134.40 < salario_bruto <= 6101.06:
    INSS = (salario_bruto)*0.14    
elif 6101.06 < salario_bruto:
    INSS = 671,12
    
base_de_calculo = (salario_bruto) - INSS - (dependentes)*189.59
if base_de_calculo < 0:
    base_de_calculo = 0

print(base_de_calculo)

if base_de_calculo <= 1903.98:
    aliquota = 0
    deduçao = 0
elif 1903.98 < base_de_calculo <= 2826.65:
    aliquota = 0.075
    deduçao = 142.80
elif 2826.65 < base_de_calculo <= 3751.05:
    aliquota = 0.15
    deduçao = 354.80
elif 3751.05 < base_de_calculo <= 4664.68:
    aliquota = 0.225
    deduçao = 636.13
elif 4664.68 < base_de_calculo:
    aliquota = 0.275
    deduçao = 869.36

IRRF = base_de_calculo * aliquota - deduçao    

print(IRRF)  