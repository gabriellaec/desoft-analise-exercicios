a=float(input('qual seu salario bruto?'))
b=int(input('quantos dependentes?'))
if a<=1045:
            inss=a*0.075
elif a<=2089.60:
            inss=a*0.09
elif a<=3134.40:
            inss=a*0.12
elif a<=6101.06:
            inss=a*0.14
else:
    inss=671.12
bdc=a-inss-(b*189.59)
if bdc<=1903.98:
            irrf=(bdc*0)
if bdc>=1903.99 and bdc<=2826.65:
            irrf=(bdc*0.075)-142.80
if bdc>=2826.66 and bdc<=3751.05:
            irrf=(bdc*0.15)-354.80
if bdc>=3751.06 and bdc<=4664.68:
            irrf=(bdc*0.225)-636.13
if bdc>=4664.69:
            irrf=(bdc*0.275)-869.36
print(irrf)
            
            
            
            
            
            
            
            
            
           
            