s=float(input("Salário bruto: "))
if s<=1045:
    inss=0.075*s
elif s<=2089.61:
    inss=0.09*s
elif s<=3134.40:
    inss=0.12*s
elif s<=6101.06:
    inss=0.14*s
else:
    inss=671.12

d=int(input("Dependentes: "))
b=s-inss-d*189.59
if b<=1903.98:
    irrf=b*0-0
elif b<=2826.65:
    irrf=b*0.075-142.8
elif b<=3751.05:
    irrf=b*0.15-354.8
elif b<=4664.68:
    irrf=b*0.225-636.13
else:
    irrf=b*0.275-869.36

print(irrf)
      