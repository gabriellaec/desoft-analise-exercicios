salario=int(input("Digite o valor do seu salário bruto: "))
dependente=int(input("Digite o numero de dependentes que voce tem: "))

def faixa_salarial(salario):
    if salario<=1045:
        return 0.075
    elif salario<=2089.6:
        return 0.09
    elif salario<=3134.4:
        return 0.12
    else:
        return 0.14
    
if salario<=6101.06:
    base=salario-(faixa_salarial(salario)*salario)-(dependente*189.59)
else:
    base=salario-(671.12)-(dependente*189.59)
    
    
def aliquota(base_calculo):
    if base_calculo<=1903.98:
        return 0
    elif base_calculo<=2826.65:
        return 0.075
    elif base_calculo<=3751.05:
        return 0.15
    elif base_calculo<=4664.68:
        return 0.225
    else:
        return 0.275
    
def deducao(base_calculo):
    if base_calculo<=1903.98:
        return 0
    elif base_calculo<=2826.65:
        return 142.8
    elif base_calculo<=3751.05:
        return 354.8
    elif base_calculo<=4664.68:
        return 636.13
    else:
        return 869.36
    
irrf=(base*aliquota(base))-deducao(base)
print("A sua contribuição para o INSS é de: ",irrf)