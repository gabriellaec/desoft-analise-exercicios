sal = int(input("Insira o salario"))
numdependentes = int(input("num de dependentes"))
#base de calculo = salario bruto - contribuicao para o INSS - num dependentes * 189,59
#IRRF = base de calculo * aliquota - deducao
#aliquota 1
if sal<= 1045.00:
    aliquota1 = 0.075
if 1045.00<sal and sal<=2089.6:
    aliquota1 = 0.09
if  2089.61<=sal and sal<= 3134.40:
    aliquota1 = 0.12
elif 3134.41<=sal and sal<= 6101.06:
    aliquota1 = 0.14
else:
    aliquota1 = 671.12/6101.06
#aliquota2

def INSS(sal,aliquota1):
    imposto = sal*aliquota1
    return imposto
def base_calculo(salario,INSS,numdependentes):
    calculo = sal - INSS(sal,aliquota1) - numdependentes*189.59
    return calculo
if base_calculo<=1903.98:
    aliquota2 = 0.0
    deducao = 0
if 1903.99<=base_calculo and base_calculo<=2826.64:
    aliquota2 = 7.5
    deducao = 142.8
if 2826.66<=base_calculo and base_calculo<=3751.05:
    aliquota2 = 0.15
    deducao = 354.80
elif 3751.06<=base_calculo and base_calculo<=4664.68:
    aliquota2 = 0.225
    deducao = 636.13
else:
    aliquota2 = 0.275
    deducao = 869.36
def IRRF(base_calculo,aliquota2,deducao):
    imposto_total = base_calculo(sal,INSS,numdependentes) * aliquota2 - deducao
    return imposto_total
    
print(IRRF(base_calculo,aliquota2,deducao))