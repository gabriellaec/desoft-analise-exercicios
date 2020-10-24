s_b=float(input('salário bruto:'))
dep=int(input('dependentes:'))
c=0
b=0
a=0
d=0
i=0
if s_b<=1045.00:
    c=s_b*0.075
    b=s_b-c-(dep*189.59)
elif s_b>=1045.01 and s_b<=2089.60:
    c=s_b*0.09
    b=s_b-c-(dep*189.59)
elif s_b>=2089.61 and s_b<=3134.40:
    c=s_b*0.12
    b=s_b-c-(dep*189.59)
elif s_b>3134.41 and s_b<=6101.06:
    c=s_b*0.14
    b=s_b-c-(dep*189.59)
else:
    c=671.12
    b=s_b-c-(dep*189.59)
if b<=1903.98:
    a=0
    d=0
    i=0
elif b>=1903.99 and b<=2826.65:
    a=0.075
    d=142.8
    i=(b*a)-d
elif b>=2826.66 and b<=3751.05:
    a=0.15
    d=354.8
    i=(b*a)-d
elif b>=3751.06 and b<=4664.68:
    a=0.225
    d=636.13
    i=(b*a)-d
else:
    a=0.275
    d=869.36
    i=(b*a)-d
print(i)
    
    