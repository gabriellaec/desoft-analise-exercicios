salario=float(input("salario bruto: "))
dependentes=int(input("numero de dependentes?: ")) 
if salario<=1045:
    contribuicao=salario*0.075
elif salario>1045 and salario<=2089.60:
    contribuicao=salario*0.09
elif salario>2089.60 and salario<=3134.40:
    contribuicao=salario*0.12
elif salario>3134.40 and salario<=6101.06:
    contribuicao=salario*0.14
elif salario>6101.06:
    contribiucao=671.12
    
base=salario-contribuicao-(dependentes*189.59)

def irrf(base):
    if base<=1903.98:
        irrf=base
        return irrf
    elif base>1903.98 and base<=2826.65:
        irrf=(base*0.075)-142
        return irrf
    elif base>2826.65 and base<=3751.05:
        irrf=(base*0.15)-354
        return irrf
    elif base>3751.05 and base<=4664.68:
        irrf=(base*0.225)-636.17
        return irrf
    elif base>4664.68:
        irff=(base*0.275)-869.36