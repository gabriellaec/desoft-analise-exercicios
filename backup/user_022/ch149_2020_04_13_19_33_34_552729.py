salario_bruto = int(input("Digite seu salario bruto: "))
dependentes = int(input("Digite a quantidade de dependentes: "))

def faixa(salario):
    if salario<=1045:
        return 0.075
    elif salario<=2089.6:
        return 0.09
    elif salario<=3134.4:
        return 0.12
    else:
        return 0.14
    
if salario_bruto<=6101.06:
    formula = salario_bruto - (faixa(salario_bruto)*salario) - (dependentes*189.59)
else:
    formula = salario_bruto-(671.12)-(dependentes*189.59)
    
    
def aliquota(base_de_calculo):
    if base_de_calculo<=1903.98:
        return 0
    elif base_de_calculo<=2826.65:
        return 0.075
    elif base_de_calculo<=3751.05:
        return 0.15
    elif base_de_calculo<=4664.68:
        return 0.225
    else:
        return 0.275
    
def deducao(base_de_calculo):
    if base_de_calculo<=1903.98:
        return 0
    elif base_de_calculo<=2826.65:
        return 142.8
    elif base_de_calculo<=3751.05:
        return 354.8
    elif base_de_calculo<=4664.68:
        return 636.13
    else:
        return 869.36
    
IRRF=(formula*aliquota(formula))-deducao(formula)
print("Sua contribuição para o INSS é de: ",IRRF)