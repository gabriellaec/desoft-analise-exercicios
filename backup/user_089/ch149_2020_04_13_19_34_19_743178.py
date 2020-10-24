salario = float(input("Qual o salário bruto?"))
numero = int(input("Qual o numero de dependentes do usuario?"))

if salario <= 1045.00:
    contribuicao = salario*0.075
    baseC = salario - contribuicao - numero*189.59
    

if 1045.01 <= salario <= 2089.60:
    contribuicao = salario*0.09
    baseC = salario - contribuicao - numero*189.59

if 2089.61 <= salario <= 3134.40:
    contribuicao = salario*0.12
    baseC = salario - contribuicao - numero*189.59
if 3134.41 <= salario <= 6101.06:
    contribuicao = salario*0.14
    baseC = salario - contribuicao - numero*189.59
if salario > 6101.06:
    contribuicao = 671.12
    baseC = salario - contribuicao - numero*189.59
    
if baseC <= 1903.98:
    IRRF = baseC*0 - 0

if 1903.99 <= baseC <= 2826.65:
    IRRF = baseC*0.075 - 142.8
if 2826.66 <= baseC <= 3751.05:
    IRRF = baseC*0.15 - 354.8
if 3751.06 <= baseC <= 4664.68:
    IRRF = baseC*0.225 - 636.13
if baseC > 4664.68:
    IRRF = baseC*0.275 - 869.36

print(IRRF)

   

    