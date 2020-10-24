    salariobruto=0
    salariobruto=float(input("qual o seu salário bruto?"))
    dependentes=int(input("qual o número de dependente?"))
    if salariobruto<=1045:
        inss=salariobruto*0.075
    elif salariobruto>= 1045.01 and salariobruto<= 2089.60:
        inss=salariobruto*0.09
    elif salariobruto >=2089.61 and salariobruto<=3134.40:
        inss=salariobruto*0.12
    elif salariobruto >=3134.41 and salariobruto<=6101.06:
        inss=salariobruto*0.14
    else:
        inss=671.12
    base=salariobruto-inss-dependentes*189.59
    if base<=1903.98:
        irrf=0
    elif base >= 1903.99 and base<= 2826.65:
        irrf=base*0.075-142.80
    elif base >= 2826.66 and base <=3751.05:
        irrf=base*0.15-354.80
    elif base >= 3751.06 and base<= 4664.68:
        irrf=base*0.225-636.13
    else:
        irrf=base*0.275-869.36
    print (irrf)

