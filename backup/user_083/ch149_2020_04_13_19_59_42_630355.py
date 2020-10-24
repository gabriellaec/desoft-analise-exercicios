a=float(input('Qual seu salario bruto: '))
b=int(input('Qual seu numero de dependentes: '))
if a<=1045:
    I=a*0.075
elif a<=2089.60:
    I=a*0.09
elif a<=3134.40:
    I=a*0.12
elif a<=6101.06:
    I=a*0.14
else:
    I=671.12
c=a-I-(b*189.59)
if c<=1903.98:
    d=0
    e=0
elif c<=2826.65:
    d=0.075
    e=142.80
elif c<=3751.05:
    d=0.15
    e=354.80
elif c<=4664.68:
    d=0.225
    e=636.13
else:
    d=0.275
    e=869.36
IRFF=(c*d)-e
print(IRFF)