salario = int(input('Qual seu salario bruto? '))
n_dep = int(input('Qual o número de dependentes? '))

def inss(s):
    if s <= 1045:
        aliq = 0.075 * s
    elif s<= 2089.6:
        aliq =0.09 * s
    elif s<= 3134.4:
        aliq =0.12 * s
    elif s<= 6101.06:
        aliq =0.14 * s
    else:
        aliq = 671.12
    return aliq

def aliquota(b):
    if b <= 1903.98:
        a = 0
    elif b <= 2826.65:
        a = 0.075
    elif b <= 3751.05:
        a = 0.15
    elif b <= 4664.68:
        a = 0.225
    else:
        a = 0.275
    return a

def deducao(b):
    if b <= 1903.98:
        d = 0
    elif b <= 2826.65:
        d = 142.8
    elif b <= 3751.05:
        d = 354.8
    elif b <= 4664.68:
        d = 636.13
    else:
        d = 869.36
    return d

base = salario - inss(salario) - (n_dep * 189.59)
irrf = base * aliquota(base) - deducao(base)
print(irrf)