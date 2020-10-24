bruto = float(input("Insira seu salário bruto: "))
dependentes = int(input("Insira o numero de dependentes: "))

if bruto <= 1045:
    aliquota = 0.075
    contribuicao = bruto * aliquota
elif bruto > 1045 and bruto <= 2089.6:
    aliquota = 0.09
    contribuicao = bruto * aliquota
elif bruto > 2089.6 and bruto <= 3134.4:
    aliquota = 0.12
    contribuicao = bruto * aliquota
elif bruto > 3134.4 and bruto <= 6101.06:
    aliquota = 0.14
    contribuicao = bruto * aliquota
else:
    contribuicao = 671.12

base_de_calculo = bruto - contribuicao - dependentes * 189.59

if base_de_calculo <= 1903.98:
    aliquota2 = 0
    deducao = 0
elif base_de_calculo > 1903.98 and base_de_calculo <= 2826.65:
    aliquota2 = 0.075
    deducao = 142.8
elif base_de_calculo > 2826.65 and base_de_calculo <= 3751.05:
    aliquota2 = 0.15
    deducao = 354.8
elif base_de_calculo > 3751.05 and base_de_calculo <= 4664.68:
    aliquota2 = 0.225
    deducao = 636.13
else:
    aliquota2 = 0.275
    deducao = 869.36
    
irrf = base_de_calculo * aliquota2 - deducao 

print("Seu imposto de renda simplificado é: {}".format(irrf))