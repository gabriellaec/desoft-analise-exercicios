salarioBruto = float(input('qual é o seu salário bruto'))
dependentes = int(input('qual é o seu número de dependentes'))
if salarioBruto <= 1045:
    inss = salarioBruto*0.075
elif salarioBruto > 1045 and salarioBruto <= 2089.6:
    inss = salarioBruto*0.09
elif salarioBruto > 2089.6 and salarioBruto <= 3134.4:
    inss = salarioBruto*0.12
elif salarioBruto > 3134.4 and salarioBruto <= 6101.06:
    inss = salarioBruto*0.14
else:
    inss = 671.12
base_de_calculo = salarioBruto - inss - (dependentes*189.59)
if base_de_calculo <= 1903.98:
    aliquota = 0
    deducao = 0
elif base_de_calculo > 1903.98 and base_de_calculo <= 2826.65:
    aliquota = 0.075
    deducao = 142.8
elif base_de_calculo > 2826.65 and base_de_calculo <= 3751.05:
    aliquota = 0.15
    deducao = 354.8
elif base_de_calculo > 3751.05 and base_de_calculo <= 4664.68:
    aliquota = 0.225
    deducao = 636.13
else:
    aliquota = 0.275
    deducao = 869.36

irrf = (base_de_calculo*aliquota) - deducao
print (irrf)

    
                     