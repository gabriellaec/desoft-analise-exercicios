salario = float(input("Qual o valor do seu salário?"))
dependentes = int(input("Qual o número de dependentes que você possui?"))

while True:
    if salario<=1045.00:
        cpi = salario*0.075
    elif 1045.01<=salario<=2089.60:
        cpi = salario*0.09
    elif 2089.61<=salario<=3134.40:
        cpi = salario*0.12
    elif 3134.41<=salario<=6101.06:
        cpi = salario*0.15
    else:
        cpi = 671.12
bdc = salario - cpi - (dependentes*189.59)
    if bdc<=1903.98:
        alq = 0.0
        ddc = 0.0
    elif 1903.99<=bdc<=2826.65:
        alq = 0.075
        ddc = 142.8
    elif 2826.66<=bdc<=3751.05:
        alq = 0.15
        ddc = 354.8
    elif 3751.06<=bdc<=4664.68:
        alq = 0.225
        ddc = 636.13
    else:
        alq = 0.275
        ddc = 869.36
irf = (bdc*alq) - ddc

return irf