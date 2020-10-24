salario = int(input("Qual o seu salário bruto: "))
dependentes = int(input("Numero de dependentes: "))

if salario <= 1045:

    base_de_calculo = salario - salario*0.075 - dependentes*189.59
    if base_de_calculo <= 1903.98:
        IRRF = base_de_calculo*0 - 0
        print (IRRF) 
    elif base_de_calculo > 1903.08 and base_de_calculo <= 2826.65:
        IRRF = base_de_calculo*0.075 - 142.80
        print (IRRF) 
    elif base_de_calculo > 2826.65 and base_de_calculo <=3751.05:
        IRRF = base_de_calculo*0.15 - 354.80
        print (IRRF)
    elif base_de_calculo > 3751.05 and base_de_calculo <=4664.68:
        IRRF = base_de_calculo*0.225 - 636.13
        print (IRRF)
    elif base_de_calculo > 4664.68:
        IRRF = base_de_calculo*0.275 - 869.36
        print (IRRF)
    
elif salario > 1045 and salario <= 2089.60:

    base_de_calculo = salario - salario*0.09 - dependentes*189.59
    if base_de_calculo <= 1903.98:
        IRRF = base_de_calculo*0 - 0
        print (IRRF)
    elif base_de_calculo > 1903.08 and base_de_calculo <= 2826.65:
        IRRF = base_de_calculo*0.075 - 142.80
        print (IRRF) 
    elif base_de_calculo > 2826.65 and base_de_calculo <=3751.05:
        IRRF = base_de_calculo*0.15 - 354.80
        print (IRRF)
    elif base_de_calculo > 3751.05 and base_de_calculo <=4664.68:
        IRRF = base_de_calculo*0.225 - 636.13
        print (IRRF)
    elif base_de_calculo > 4664.68:
        IRRF = base_de_calculo*0.275 - 869.36
        print (IRRF)
 
elif salario > 2089.60 and salario <=3134.40:
    
    base_de_calculo = salario - salario*0.12 - dependentes*189.59
    if base_de_calculo <= 1903.98:
        IRRF = base_de_calculo*0 - 0
        print (IRRF) 
    elif base_de_calculo > 1903.08 and base_de_calculo <= 2826.65:
        IRRF = base_de_calculo*0.075 - 142.80
        print (IRRF) 
    elif base_de_calculo > 2826.65 and base_de_calculo <=3751.05:
        IRRF = base_de_calculo*0.15 - 354.80
        print (IRRF)
    elif base_de_calculo > 3751.05 and base_de_calculo <=4664.68:
        IRRF = base_de_calculo*0.225 - 636.13
        print (IRRF)
    elif base_de_calculo > 4664.68:
        IRRF = base_de_calculo*0.275 - 869.36
        print (IRRF)

elif salario > 3134.40 and salario <=6101.06:
    
    base_de_calculo = salario - salario*0.14 - dependentes*189.59
    if base_de_calculo <= 1903.98:
        IRRF = base_de_calculo*0 - 0
        print (IRRF) 
    elif base_de_calculo > 1903.08 and base_de_calculo <= 2826.65:
        IRRF = base_de_calculo*0.075 - 142.80
        print (IRRF) 
    elif base_de_calculo > 2826.65 and base_de_calculo <=3751.05:
        IRRF = base_de_calculo*0.15 - 354.80
        print (IRRF)
    elif base_de_calculo > 3751.05 and base_de_calculo <=4664.68:
        IRRF = base_de_calculo*0.225 - 636.13
        print (IRRF)
    elif base_de_calculo > 4664.68:
        IRRF = base_de_calculo*0.275 - 869.36
        print (IRRF)
        
elif salario > 6101.06: 
    
    base_de_calculo = salario - 671.12 - dependentes*189.59
    if base_de_calculo <= 1903.98:
        IRRF = base_de_calculo*0 - 0
        print (IRRF) 
    elif base_de_calculo > 1903.08 and base_de_calculo <= 2826.65:
        IRRF = base_de_calculo*0.075 - 142.80
        print (IRRF) 
    elif base_de_calculo > 2826.65 and base_de_calculo <=3751.05:
        IRRF = base_de_calculo*0.15 - 354.80
        print (IRRF)
    elif base_de_calculo > 3751.05 and base_de_calculo <=4664.68:
        IRRF = base_de_calculo*0.225 - 636.13
        print (IRRF)
    elif base_de_calculo > 4664.68:
        IRRF = base_de_calculo*0.275 - 869.36
        print (IRRF)