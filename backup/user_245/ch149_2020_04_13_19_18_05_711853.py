#Faça um programa que pergunta o salário bruto e o número de dependentes do usuário e imprime o seu Imposto de Renda Retido na Fonte (IRRF) simplificado. O cálculo do IRRF simplificado depende do valor da contribuição para o INSS e da base de cálculo.
 #PERGUNTA O SALARIO
sal = int(input("Insira o salario"))
numdependentes = int(input("num de dependentes"))
#base de calculo = salario bruto - contribuicao para o INSS - num dependentes * 189,59
#IRRF = base de calculo * aliquota - deducao
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
def INSS(sal,aliquota1):
    imposto = sal*aliquota1
    return imposto
def base_calculo(salario,INSS,numdependentes):
    calculo = sal - INSS(sal,aliquota1) - numdependentes*189.59
    return calculo
def IRRF(base_calculo,aliquota2,deducao):
    imposto_total = base_calculo(sal,INSS,numdependentes) * aliquota2 - deducao
    return imposto_total