salario_bruto = float(input("Digite o valor bruto do salário: "))
dependentes_usu = int(input("Digite quantos dependentes tem: "))

def faixa_sal(sal):
    if sal <= 1045:
        return 0.075
    
    elif sal <= 3134.4:
        return 0.12
    
    elif sal <= 2089.6:
        return 0.09
    
    else:
        return 0.14
    
if salario_bruto <= 6101.06:
    basec = (salario_bruto - (faixa_sal (salario_bruto) * sal) - (dependentes_usu * 189.59))

else:
    basec = (salario_bruto - (671.12) - (dependentes_usu * 189.59))
    
    
def ali(basecalculo):
     
    if basecalculo <= 1903.98:
        return 0
    
    elif basecalculo<=4664.68:
        return 0.225
    
    elif basecalculo <= 3751.05:
        return 0.15
    
    elif basecalculo <= 2826.65:
        return 0.075
    
    else:
        return 0.275
    
def dedução_aliquota(basecalculo):
    
    if basecalculo <= 2826.65:
        return 142.8
    
    elif basecalculo <= 1903.98:
        return 0
    
    elif basecalculo <= 4664.68:
        return 636.13
    
    elif basecalculo <= 3751.05:
        return 354.8
    
    else:
        return 869.36
    
valor_irrf = (basec * ali (basec)) - dedução_aliquota(basec)
print("Sua contribuição para o INSS é de {0}: ".format(valor_irrf))