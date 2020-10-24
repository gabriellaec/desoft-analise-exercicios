s_b=float(input('salário bruto:'))
dep=int(input('dependentes:'))
c=0
b=0
a=0
d=0
i=0
if s_b<=1045:
    c=s_b*0.075
    b=s_b-c-dep*189.59
elif s_b>1045 and s_b<=2089.6:
    c=s_b*0.09
    b=s_b-c-dep*189.59
elif s_b>2089.6 and s_b<=3134.4:
    c=s_b*0.012
    b=s_b-c-dep*189.59
elif s_b>3134.4 and s_b<=6101.06:
    c=s_b*0.014
    b=s_b-c-dep*189.59
else:
    c=671.12
    b=s_b-c-dep*189.59
if b<=1903.98:
    a=0
    d=0
    i=0
elif b>1903.98 and b<=2826.65:
    a=0.075
    d=142.8
    i=b*a-d
elif b>2826.65 and b<=3751.05:
    a=0.15
    d=354.8
    i=b*a-d
elif b>3751.05 and b<=4664.68:
    a=0.225
    d=636.13
    i=b*a-d
else:
    a=0.275
    d=869.36
    i=b*a-d
print(i)
    
    