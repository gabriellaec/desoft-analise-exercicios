salario_bruto = int(input('Qual o seu salário bruto? '))
n_dependentes = int (input("Quantos são os dependentes da sua renda? "))



def calcula_imposto (salario_bruto, n_dependentes):
    #contribuição
    if salario_bruto <= 1045:
        contribuicao = (7.5/100)*salario_bruto
    elif salario_bruto >= 1045.01 and salario_bruto <= 2089.60:
        contribuicao = 9/100*salario_bruto
    elif salario_bruto >= 2089.61 and salario_bruto <= 3134.40:
        contribuicao = 12/100*salario_bruto
    elif salario_bruto >= 3134.41 and salario_bruto <= 6101.06:
        contribuicao = 14/100*salario_bruto
    elif salario_bruto > 6101.06:
        contribuicao = 671.12
    #base de calculo
    base_de_calculo = salario_bruto - contribuicao - n_dependentes*(189.59)
    
    #alíquota e dedução
    if base_de_calculo <= 1903.98:
        aliquota = 0
        deducao = 0
    elif base_de_calculo >= 1903.99 and base_de_calculo <= 2826.65:
        aliquota = 7.5/100
        deducao = 142.80
    elif base_de_calculo >= 2826.66 and base_de_calculo <= 3751.05:
        aliquota = 15/100
        deducao = 354.80
    elif base_de_calculo >= 3751.06 and base_de_calculo <= 4664.68:
        aliquota = 22.5/100
        deducao = 636.13
    elif base_de_calculo > 4664.68:
        aliquota = 27.5/100
        deducao = 869.36

    #IRRF:
    imposto = base_de_calculo*aliquota - deducao

    return imposto