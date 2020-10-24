I=0
a=int(input('Qual seu salario bruto: '))
b=int(input('Qual seu numero de dependentes: '))
if a<=1045:
    I=a*0.075
if 1045<a<=2089.60:
    I=a*0.09
if 2089.60<a<=3134.40:
    I=a*0.12
if  3134.40<a<=6101.06:
    I=a*0.14
else:
    I=671.12
c=a-I-b*189.59
IRFF=0
if c<=1903.98:
    IRFF=c
if 1903.98<c<=2826.65:
    IRFF=c*0.075-142.80
if 2826.65<c<=3751.05:
    IRFF=c*0.15-354.80
if 3751.05<c<=4664.68:
    IRFF=c*0.225-636.13
else:
    IRFF=c*0.275-869.36