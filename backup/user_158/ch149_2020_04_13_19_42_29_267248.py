#Pergunta 
salario_bruto = float(input('Qual eh seu Salario Bruto? '))
n_dependentes = int(input('Quantos dependentes voce possui? '))

#caucula o inss
if salario_bruto <= 1045.00:
    inss = salario_bruto*0.075
if salario_bruto > 1045.00 and salario_bruto <= 2089.61:
    inss = salario_bruto*0.09
if salario_bruto < 2089.61 and salario_bruto <= 3134.40:
    inss = salario_bruto*0.12
if salario_bruto < 3134.40 and salario_bruto <= 6101.06:
    inss = salario_bruto*0.14
if salario_bruto < 6101.06:
    inss = 671,12

#Base do cauculo 
base_do_cauculo = salario_bruto - inss - n_dependentes*189,59

#caucula irrf
if salario_bruto <= 1903.98 :
    irrf = 0
if salario_bruto > 1903.98 and salario_bruto <= 2826.65:
     irrf = base_do_cauculo*0.075 -142.80
if salario_bruto < 2826.65 and salario_bruto <= 3751.05:
    irrf = base_do_cauculo*0.15 -354.80
if salario_bruto < 3751.05 and salario_bruto <= 4664.68:
     irrf = base_do_cauculo*0.225 -636.13
if salario_bruto < 4664,68:
     irrf = base_do_cauculo*0.275 -869.36

print(' O seu Imposto de Renda Retido na Fonte (IRRF) simplificado eh {0}'.format(irrf))