salario_bruto = float(input("Qual o seu salário bruto? "))
n_de_dependentes = int(input("Quantos dependentes vc possui? "))

def INSS(salario_bruto):
    if salario_bruto < 1045:
        inss = salario_bruto*0.075
    elif  1045.01 < salario_bruto < 2089.60:
        inss = salario_bruto*0.09
    elif 2089.61 < salario_bruto < 3134.40:
        inss = salario_bruto*0.12
    elif 3134.41 < salario_bruto < 6101.06:
        inss = salario_bruto*0.14
    else:
        inss = 671.12
    return salario_bruto 
inss = salario_bruto   
    
def base_de_calculo(inss):
    bc = salario_bruto - inss - n_de_dependentes * 189,59
    return bc
base = base_de_calculo(inss)



def al_ded(base):
    if base < 1903.98:
        aliquota = 0
        ded = 0
    elif 1903.99 < base < 2826.65:
        aliquota = base*0.075
        ded = 142.8
    elif 2826.66 < base < 3751.05:
        aliquota = base*0.15
        ded = 354.8
    elif 3751.06 < base < 4664.68:
        aliquota = base*0.225
        ded = 636.13
    else:
        aliquota = base*0.275
        ded = 869.36
    return base


def imposto(base,aliquota,ded):
    irff = base * aliquota - ded
    return irff 

IRFF = imposto(base,aliquota,ded)
print('O seu IRRF simplificado é de {} reais'.format(IRFF))