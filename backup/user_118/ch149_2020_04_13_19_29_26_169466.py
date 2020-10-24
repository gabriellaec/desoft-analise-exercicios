salario=float(input('Qual o salario bruto? '))
dependentes=int(input('Quantos dependentes? '))
if salario<=1045.00:
    b=salario*0.075
    base=salario-b-(dependentes*189.59)
    return base 
elif 1045.01<salario<2089.60:
    b=salario*0.09
    base=salario-b-(dependentes*189.59)
    return base 
elif 2089.61<=salario<=3134.40:
    b=salario*0.12
    base=salario-b-(dependentes*189.59)
    return base 
elif 3134.41<=salario<=6101.06:
    b=salario*0.14
    base=salario-b-(dependentes*189.59)
    return base 
elif salario>6101.06
    b=671.12
    base=salario-b-(dependentes*189.59)
    return base 
if base<=1903.98:
    irff=base
elif 1903.99<=base<=2826.65:
    irrf=(base*0.075)-142.80
elif 2826.66<=base<=3751.05:
    irrf=(base*0.15)-354.80
elif 3751.06<=base<=4664.68:
    irrf=(base*0.225)-636.13
elif base>4664.80:
    irff=(base*0.275)-869.36
    
    