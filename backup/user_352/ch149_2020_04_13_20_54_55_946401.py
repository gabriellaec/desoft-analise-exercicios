salario_bruto=float(input("qual o seu salário bruto?"))
numero_dependentes=int(input("quantos dependentes você possui?"))


    if salario_bruto>6101.06:
        inss = 671.12
    elif salario_bruto<=1045.00:
        inss = salario_bruto*0.075
    elif salario_bruto>1045.00 and salario_bruto<=2089.60:
        inss = salario_bruto*0.09
    elif salario_bruto>3134.40 and salario_bruto<=6101.06:
        inss = salario_bruto*0.14
    else:
        inss = salario_bruto*0.12
    base_de_calculo = salario_bruto - inss - (numero_dependentes*189.59)
    if  base_de_calculo<=1903.98:
        aliquota=0
        deducao=0
    elif  base_de_calculo>1903.98 and base_de_calculo<=2826.65:
        aliquota=0.075
        deducao=142.80
    elif  base_de_calculo>2826.65 and  base_de_calculo<=3751.05:
        aliquota=0.15
        deducao=354.80
    elif  base_de_calculo>3751.05 and  base_de_calculo<=4664.65:
        aliquota=0.225
        deducao=636.13
    else:
        aliquota=0.275
        deducao=869.36
    irrf = (base_de_calculo*aliquota)-deducao
    print(irrf)

    
        