salario=float(input('Qual salario bruto?'))
nd=int(input('Qual seu nemero de dependentes?'))
if salario <= 1045:
    irrf=salario-salario*0.075
    print (irrf)
if 1045.01<=salario<=2089.6:
    irrf2=salario-salario*0.09
    print (irrf2)
if 2089.61<=salario<=3134.4:
    bc=salario-salario*0.12-nd*189.59
    if bc<=1903.98:
        print(bc)
    if 1903.99<=bc<=2826.65:
        irrf3=bc*0.075-142.8
        print (irrf3)
if 3134.41<=salario<=6101.06:
    bc=salario-salario*0.14-nd*189.59
    if bc<=1903.98:
        print(bc)
    if 1903.99<=bc<=2826.65:
        irrf3=bc*0.075-142.8
        print (irrf3)
    if 2826.66<=bc<=3751.05:
        irrf4=bc*0.15-354.8
        print (irrf4)
if salario>6101.06:
    bc=salario-671.12-nd*189.59
    if bc<=1903.98:
        print(bc)
    if 1903.99<=bc<=2826.65:
        irrf3=bc*0.075-142.8
        print (irrf3)
    if 2826.66<=bc<=3751.05:
        irrf4=bc*0.15-354.8
        print (irrf4)
    if 3751.06<=bc<=4664.68:
        irrf5=bc*0.225-636.13
        print (irrf5)
    if salario>4664.68:
        irrf6=bc*0.275-869.36
        print (irrf6)