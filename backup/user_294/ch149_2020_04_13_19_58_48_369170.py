salario_bruto=float(input('qual seu salrio bruto?: '))
dependentes=int(input('qual o numero de dependentes?: '))
def base_de_calculo(salario_bruto):
    if salario_bruto <= 1045:
        contribuicao == 0.075*salario_bruto
    elif salario_bruto >1045 and salario_bruto < 2089.60:
        contribuicao == 0.09*salario_bruto
    elif salario_bruto > 2089.60 and salario_bruto < 3134.40:
        contribuicao == 0.12*salario_bruto
    elif salario_bruto > 3134.40 and salario_bruto < 6101.06:
        contribuicao == 0.14*salario_bruto
    else:
        contribuicao == 671.12
    x= salario_bruto - contribuicao - dependentes*189.59
    return x
def IRRF(base_de_calculo):
    if base_de_calculo <= 1903.98:
        aliquota == 0
        deducao == 0
    elif base_de_calculo > 1903.98 and base_de_calculo < 2826.65:
        aliquota == 0.075
        deducao == 142.80
    elif base_de_calculo > 2826.65 and base_de_calculo < 3751.05:
        aliquota == 0.15
        deducao == 354.80
    elif base_de_calculo > 3751.05 and base_de_calculo < 4664.68:
        aliquota == 0.225
        deducao == 636.13
    else:
        aliquota == 0.275
        deducao == 869.36
    y= base_de_calculo*aliquota - deducao
    return y
print (IRRF(base_de_calculo))

        