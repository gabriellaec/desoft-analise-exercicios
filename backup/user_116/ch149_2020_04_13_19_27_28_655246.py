salariob=float(input("salario"))
dependentes=int(input("dependentes"))
if salariob<=1045:
    al=(7.5/100)*salariob
elif salariob>1045 and salariob<=2089.60:
    al=(9/100)*salariob
elif salariob>2089.60 and salariob<=3143.40:
    al=(12/100)*salariob
elif salariob>3143.40 and salariob<=6101.06: 
    al=(14/100)*salariob
elif salariob> 6101.06:
    al=671.12
base=(salariob)-(al)-dependentes*189.59

if base <=1903.98:
    al2=0
    de=0
elif base>1903.98 and base<=2826.65:
    al2=(7.5/100)
    de=142.8
elif base>2826.65 and base<=3751.05:
    al2=15/100
    de=354.8
elif base>3751.05 and base<=4664.68:
    al2=22.5/100
    de=636.13
elif base>4664.68:
    al2=27.5/100
    de=869.36
irrf=base*al2-de
print(irrf)