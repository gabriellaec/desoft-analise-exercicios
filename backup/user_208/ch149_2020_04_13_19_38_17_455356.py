salario = int(input("Digite o seu salário: "))
numero_de_dependentes = int(input("Qual o número de dependentes? "))
if salario <= 1045:
    base_de_calculo = salario - (salario*0.075) - (numero_de_dependentes * 189.59)
    if base_de_calculo <= 1903.98:
        irrf = base_de_calculo *0-0
        print("O valor do IRRF é {}".format(irrf))
    elif base_de_calculo >= 1903.99 and base_de_calculo <= 2826.65:
        irrf = base_de_calculo * 0.075 - 142.80
        print("O valor do IRRF é {}".format(irrf))
    elif base_de_calculo >= 2826.66 and base_de_calculo <= 3751.05:
        irrf = base_de_calculo * 0.15 - 354.80
        print("O valor do IRRF é {}".format(irrf))
    elif base_de_calculo >= 3751.06 and base_de_calculo <= 4664.68:
        irrf = base_de_calculo * 0.225 - 636.13
        print("O valor do IRRF é {}".format(irrf))
    else:
        irrf = base_de_calculo * 0.275 - 869.36
        print("O valor do IRRF é {}".format(irrf))
elif salario >= 1045.01 and salario <= 2089.60:
    base_de_calculo = salario - (salario*0.09) - (numero_de_dependentes*189.59)
    if base_de_calculo <= 1903.98:
        irrf = base_de_calculo *0-0
        print("O valor do IRRF é {}".format(irrf))
    elif base_de_calculo >= 1903.99 and base_de_calculo <= 2826.65:
        irrf = base_de_calculo * 0.075 - 142.80
        print("O valor do IRRF é {}".format(irrf))
    elif base_de_calculo >= 2826.66 and base_de_calculo <= 3751.05:
        irrf = base_de_calculo * 0.15 - 354.80
        print("O valor do IRRF é {}".format(irrf))
    elif base_de_calculo >= 3751.06 and base_de_calculo <= 4664.68:
        irrf = base_de_calculo * 0.225 - 636.13
        print("O valor do IRRF é {}".format(irrf))
    else:
        irrf = base_de_calculo * 0.275 - 869.36
        print("O valor do IRRF é {}".format(irrf))
elif salario >= 2089.61 and salario <= 3134.40:
    base_de_calculo = salario - (salario*0.12) - (numero_de_dependentes*189.59)
    if base_de_calculo <= 1903.98:
        irrf = base_de_calculo *0-0
        print("O valor do IRRF é {}".format(irrf))
    elif base_de_calculo >= 1903.99 and base_de_calculo <= 2826.65:
        irrf = base_de_calculo * 0.075 - 142.80
        print("O valor do IRRF é {}".format(irrf))
    elif base_de_calculo >= 2826.66 and base_de_calculo <= 3751.05:
        irrf = base_de_calculo * 0.15 - 354.80
        print("O valor do IRRF é {}".format(irrf))
    elif base_de_calculo >= 3751.06 and base_de_calculo <= 4664.68:
        irrf = base_de_calculo * 0.225 - 636.13
        print("O valor do IRRF é {}".format(irrf))
    else:
        irrf = base_de_calculo * 0.275 - 869.36
        print("O valor do IRRF é {}".format(irrf))      
elif salario >= 3134.41 and salario <= 6101.06:
    base_de_calculo = salario - (salario*0.14) - (numero_de_dependentes*189.59)
    if base_de_calculo <= 1903.98:
        irrf = base_de_calculo *0-0
        print("O valor do IRRF é {}".format(irrf))
    elif base_de_calculo >= 1903.99 and base_de_calculo <= 2826.65:
        irrf = base_de_calculo * 0.075 - 142.80
        print("O valor do IRRF é {}".format(irrf))
    elif base_de_calculo >= 2826.66 and base_de_calculo <= 3751.05:
        irrf = base_de_calculo * 0.15 - 354.80
        print("O valor do IRRF é {}".format(irrf))
    elif base_de_calculo >= 3751.06 and base_de_calculo <= 4664.68:
        irrf = base_de_calculo * 0.225 - 636.13
        print("O valor do IRRF é {}".format(irrf))
    else:
        irrf = base_de_calculo * 0.275 - 869.36
        print("O valor do IRRF é {}".format(irrf))
else:
    base_de_calculo = salario - 671.12 - (numero_de_dependentes*189.59)
    if base_de_calculo <= 1903.98:
        irrf = base_de_calculo *0-0
        print("O valor do IRRF é {}".format(irrf))
    elif base_de_calculo >= 1903.99 and base_de_calculo <= 2826.65:
        irrf = base_de_calculo * 0.075 - 142.80
        print("O valor do IRRF é {}".format(irrf))
    elif base_de_calculo >= 2826.66 and base_de_calculo <= 3751.05:
        irrf = base_de_calculo * 0.15 - 354.80
        print("O valor do IRRF é {}".format(irrf))
    elif base_de_calculo >= 3751.06 and base_de_calculo <= 4664.68:
        irrf = base_de_calculo * 0.225 - 636.13
        print("O valor do IRRF é {}".format(irrf))
    else:
        irrf = base_de_calculo * 0.275 - 869.36
        print("O valor do IRRF é {}".format(irrf))