salario_b = float(input("Qual o valor do seu salário?" ))
dependentes = int(input("Qual o número de dependentes que você possui?" ))


if salario_b<=1045.00:
    cont = salario_b*0.075
elif 1045.01<=salario_b<=2089.60:
    cont = salario_b*0.09
elif 2089.61<=salario_b<=3134.40:
    cont = salario_b*0.12
elif 3134.41<=salario_b<=6101.06:
    cont = salario_b*0.14
else:
    cont = 671.12

bdc = salario_b - cont - (dependentes*189.59)

if bdc<=1903.98:
    al = 0.0
    ded = 0.0
elif 1903.99<=bdc<=2826.65:
    al = 0.075
    ded = 142.8
elif 2826.66<=bdc<=3751.05:
    al = 0.15
    ded = 354.8
elif 3751.06<=bdc<=4664.68:
    al = 0.225
    ded = 636.13
else:
    al = 0.275
    ded = 869.36

irrf = (bdc*al) - ded

print (irrf)
