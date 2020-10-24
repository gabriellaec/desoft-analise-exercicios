a=float(input("Qual o seu salário bruto?"))
b=int(input("Qual o número de dependentes?"))
if a<=1045:
    inss=a*0.075
elif a<=2089.6:
    inss=a*0.09
elif a<=3134.41:
    inss=a*0.12
elif a<=6101.06:
    inss=a*0.14
else:
    inss=671.12
base=a-inss-(b*189.59)
if base<=1903.98:
    irrf=(base*0)+0
elif base<=2826.65:
    irrf=(base*0.075)-142.8
elif base<=3751.05:
    irrf=(base*0.15)-354.8
elif base<=4664.68:
    irrf=(base*0.225)-636.13
else:
    irrf=(base*0.275)-869.36
print (irrf)