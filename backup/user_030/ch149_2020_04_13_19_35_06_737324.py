salari0 = int(input("Qual seu salario bruto? "))

dependentes = int(input("Quantas pessoas dependem do seu salario? "))


def faixa(salari0):
    if salari0 <= 1045:
        return 0.075
    elif salari0 <= 2089.6:
        return 0.09
    elif salari0 <= 3134.4:
        return 0.12
    else:
        return 0.14
    
    
if salari0 <= 6101.06:
    base = salari0-(faixa(salari0)*salari0) - (dependentes*189.59)
else:
    base = salari0-(671.12) - (dependentes*189.59)
    
   

def aliq(basedecalc):
    if basedecalc <= 1903.98:
        return 0
    elif basedecalc <= 2826.65:
        return 0.075
    elif basedecalc <= 3751.05:
        return 0.15
    elif basedecalc <= 4664.68:
        return 0.225
    else:
        return 0.275
    
    
def aliqded(basedecalc):
    if basedecalc <= 1903.98:
        return 0
    elif basedecalc <= 2826.65:
        return 142.8
    elif basedecalc <= 3751.05:
        return 354.8
    elif basedecalc <= 4664.68:
        return 636.13
    else:
        return 869.36
    
irrf = (base*aliq(base)) - aliqded(base)

print("Contribuição para o INSS: ",irrf)