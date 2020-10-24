def inss(salario,dependentes):
    if salario<=1045.00:
        valor_inss=salario*0.075
    elif 1045.01<=salario<=2089.60:
        valor_inss=salario*0.09
    elif 2089.61<=salario<=3134.40:
        valor_inss=salario*0.12
    elif 3134.41<=salario<=6101.06:
        valor_inss=salario*0.14
    else:
        valor_inss=671.12
    base_de_calculo=salario-valor_inss-dependentes*189.59
    return base_de_calculo

 
def irrf(salario,dependentes):
    salario=float(input("Digite seu salário bruto: "))
    dependentes=int(input("Quantos dependentes dessa renda? "))
    base=inss(salario,dependentes)
    if base<=1903.98:
        valor_final=0
        print(0)
    elif 1903.99<=base<=2826.65:
        valor_final=base*0.075-142.80
    elif 2826.66<=base<=3751.05:
        valor_final=base*0.15-354.80
    elif 3751.06<=base<=4664.68:
        valor_final=base*0.225-636.13
    else:
        valor_final=base*0.275-869.36
    print ('Seu IRFF é de: {0}'.format(valor_final)) 