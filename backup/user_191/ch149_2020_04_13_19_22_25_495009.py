salbrut=float(input('Qual é seu salário?'))
dep=int(input('Qual é o número de dependentes?'))
if salbrut<=1045:
    bc=salbrut-salbrut*0.075-dep*189.59
elif salbrut<=2086.60:
    bc=salbrut-salbrut*0.09-dep*189.59
elif salbrut<=3134.40:
    bc=salbrut-salbrut*0.12-dep*189.59
elif salbrut<=6101.06:
    bc=salbrut-salbrut*0.14-dep*189.59
else:
    bc=salbrut-671.12-dep*189.59
if bc<=1903.98:
    irrf=bc*0-0
elif bc<=2826.65:
    irrf=bc*0.075-142.80
elif bc<=3751.05:
    irrf=bc*0.15-354.80
elif bc<=4664.68:
    irrf=bc*0.225-636.13
else:
    irrf=bc*0.275-869.36
print(irrf)