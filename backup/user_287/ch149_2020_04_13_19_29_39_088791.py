salario_bruto = int(input('Seu salário bruto: '))
n_dependentes=int(input('Quantos dependentes: ' ))

def faixa(sal):
    if sal <= 1045:
        return 0.075
    elif sal <= 2089.6:
        return 0.09
    elif sal <= 3134.4:
        return 0.12
    else:
        return 0.14
    
if salario_bruto <= 6101.06:
    b=salario_bruto-(faixa(salario_bruto)*sal)-(n_dependentes*189.59)
else:
    b=salario_bruto-(671.12)-(n_dependentes*189.59)
    
def deducao(c):
    if c<=1903.98:
        return 0
    elif c<=2826.65:
        return 142.8
    elif c<=3751.05:
        return 354.8
    elif c<=4664.68:
        return 636.13
    else:
        return 869.36
def aliquota(d):
    if d<=1903.98:
        return 0
    elif d<=2826.65:
        return 0.075
    elif d<=3751.05:
        return 0.15
    elif d<=4664.68:
        return 0.225
    else:
        return 0.275
    
IRRF=(b*aliquota(b))-ded(b)
print("Sua contribuição para o INSS é de: ",IRRF)