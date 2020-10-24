def contribuicao_INSS(salario):
    if salario <= 1045:
        return salario * 0.075
    if salario <= 2089.60:
        return salario * 0.09
    if salario <= 3134.40:
        return salario * 0.12
    if salario <= 6101.06:
        return salario * 0.14
    else:
        return 671.12

def IRRF(base):
    if base <= 1903.98:
        return 0.0
    if base <= 2826.65:
        return base*0.075 - 142.80
    if base <= 3751.05:
        return base*0.15 - 354.80
    if base <= 4664.68:
        return base*0.225 - 636.13
    return base*0.275 - 869.36


salario = float(input("Informe o o salário bruto: "))
dependentes = int(input("Informe o número de dependentes: "))

base = salario - contribuicao_INSS(salario) - dependentes * 189.59

print(IRRF(base))