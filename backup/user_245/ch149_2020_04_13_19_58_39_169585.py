salario = float(input("Insira o salario"))
num_pendentes = int(input("num de dependentes"))
#base de calculo = salario bruto - contribuicao para o INSS - num dependentes * 189,59
#IRRF = base de calculo * aliquota - deducao
#aliquota 1
if salario<= 1045.00:
    INSS = salario * 0.075
if 1045.00<salario and salario<=2089.6:
    INSS = sal * 0.09
if  2089.61<=salario and salario<= 3134.40:
    INSS = sal * 0.12
elif 3134.41<=salario and salario<= 6101.06:
    INSS = salario * 0.14
else:
    INSS = 671.12

base_de_calculo = sal-INSS-num_pendentes*189.59
if base_de_calculo<=1903.98:
    aliquota2 = 0.0
    deducao = 0
if 1903.99<=base_de_calculo and base_de_calculo<=2826.64:
    aliquota2 = 7.5
    deducao = 142.8
if 2826.66<=base_de_calculo and base_de_calculo<=3751.05:
    aliquota2 = 0.15
    deducao = 354.80
elif 3751.06<=base_de_calculo and base_de_calculo<=4664.68:
    aliquota2 = 0.225
    deducao = 636.13
else:
    aliquota2 = 0.275
    deducao = 869.36
irff = base_de_calculo*aliquota2-deducao
print(irff)