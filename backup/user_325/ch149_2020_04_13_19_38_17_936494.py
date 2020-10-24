salario_bruto = float(input("Digite seu salário bruto: "))
dependentes_usu = int(input("Digite quantos dependentes tem: "))

def faixa_sal(salario_bruto):
    
    if salario_bruto <= 1045:
        return 0.075
    
    elif salario_bruto <= 2089.6:
        return 0.09
    
    elif salario_bruto <= 3134.4:
        return 0.12
    
    else:
        return 0.14
    
if salario_bruto <= 6101.06:
    base = salario_bruto-(faixa_sal(salario_bruto)*salario_bruto) - (dependentes_usu*189.59)

else:
    base = salario_bruto-(671.12) - (dependentes_usu*189.59)
    
    
def aliquota(basecalc):
    
    if basecalc <= 1903.98:
        return 0
    
    elif basecalc <= 2826.65:
        return 0.075
    
    elif basecalc <= 3751.05:
        return 0.15
    
    elif basecalc <= 4664.68:
        return 0.225
    
    else:
        return 0.275
    
def dedução_aliquota(basecalc):
    
    if basecalc <= 1903.98:
        return 0
    
    elif basecalc <= 2826.65:
        return 142.8
    
    elif basecalc <= 3751.05:
        return 354.8
    
    elif basecalc <= 4664.68:
        return 636.13
    
    else:
        return 869.36
    
irrf = (base*aliquota(base)) - dedução_aliquota(base)

print("Sua contribuição para o inss é de {0}: ".format(irrf))