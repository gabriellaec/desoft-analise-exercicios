def contribuicao_inss(salario):
    aliquota = 7.5/100
    if  1045 < salario <= 2089.6:
          aliquota = 9/100
    elif 2089.6 < salario <= 3134.4:
        aliquota = 12/100
    elif 3134.4 < salario <= 6101.06:
        aliquota = 14/100
    elif salario > 6101.06:
        return 671.12
    return aliquota * salario


def aliquota_pra_base(base):
    aliquota = 0
    if 1903.98 < salario <= 2826.65:
        aliquota = 7.5/100
    elif 2826.65 < salario <= 3751.05:
        aliquota = 15/100
    elif 3751.05 < salario <= 4664.68:
        aliquota = 22.5/100
    elif salario > 4664.68:
        aliquota = 27.5
    return aliquota

def deducao_pra_base(base):
    deducao = 0
    if 1903.98 < salario <= 2826.65:
        deducao = 142.8
    elif 2826.65 < salario <= 3751.05:
        deducao = 354.8
    elif 3751.05 < salario <= 4664.68:
        deducao = 636.13
    elif salario > 4664.68:
        deducao = 869.36
    return deducao

salario = float(input("qual seu salario?"))
dependentes = int(input("quantos dependentes voce tem?"))

base = salario - contribuicao_inss(salario) - dependentes * 189.59
irrf = base * aliquota_pra_base(base) - deducao_pra_base(base)
print(irrf)