salario_bruto= int(input('Salário bruto: '))
numero_dependentes = int(input('Quantos dependentes tem: '))

def f(salario_bruto):
    if salario_bruto <= 1045:
        return 0.075
    elif salario_bruto <= 2089.6:
        return 0.09
    elif salario_bruto <= 3134.4:
        return 0.12
    else:
        return 0.14
    
if salario_bruto <= 6101.06:
    b = salario_bruto-(f(salario_bruto)*salario_bruto) - (numero_dependentes*189.59)
else:
    b = salario_bruto-(671.12) - (numero_dependentes*189.59)
    
    
def a(calculo):
    if calculo <= 1903.98:
        return 0
    elif calculo <= 2826.65:
        return 0.075
    elif calculo <= 3751.05:
        return 0.15
    elif calculo <= 4664.68:
        return 0.225
    else:
        return 0.275
    
def deducao(x):
    if x<= 1903.98:
        return 0
    elif x <= 2826.65:
        return 142.8
    elif x <= 3751.05:
        return 354.8
    elif x <= 4664.68:
        return 636.13
    else:
        return 869.36
    
IRRF = (b*a(b)) - deducao(b)
print('Contribuicao INSS: ',IRRF)