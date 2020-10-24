salario_bruto = float(input("Digite seu salario bruto: "))
dependentes = int(input("Digite o numero de dependentes: "))

if salario_bruto <= 1045.00:
    al = salario_bruto*0.075
elif salario_bruto > 1045.00 and salario_bruto <= 2089.60:
    al = salario_bruto*0.09
elif salario_bruto > 2089.60 and salario_bruto <= 3134.40:
    al = salario_bruto*0.12
elif salario_bruto > 3134.40 and salario_bruto <= 6101.06:
    al = salario_bruto*0.14
else:
    al = 671.12

base_de_calculo = salario_bruto + (- al) + (- (dependentes*189.59)) 

if base_de_calculo <= 1903.98:
    ali = 0.00
    de = 0.00
elif base_de_calculo > 1903.98 and base_de_calculo <= 2826.65:
    ali = 0.075
    de = 142.80
elif base_de_calculo > 2826.65 and base_de_calculo <= 3751.05:
    ali = 0.15
    de = 354.80
elif base_de_calculo > 3751.05 and base_de_calculo <= 4664.68:
    ali = 0.225
    de = 636.13
else:
    ali = 0.275
    de = 869.36
    
IRRF = base_de_calculo*ali + (- de)

print(IRRF)