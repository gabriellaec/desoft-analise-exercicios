s=float(input('qual o salário?'))
d=float(input('quantos dependentes?'))
def base(s,d):
    if s <=1045:
        a=0.075
        base=s-a*s-d*189.59
    elif 1045<s<=2089.60:
        a=0.09
        base=s-a*s-d*189.59
    elif 2089.60<s<=3134.40:
        a=0.12
        base=s-a*s-d*189.59
    elif 3134.40<s<=6101.06:
        a=0.14
        base=s-a*s-d*189.59
    else:
        a=671.12
        base=s-a-d*189.59
    return base
def irrf(base):
    if base<=1903.98:
        a=0
        de=0
        irrf=base*a-de
    elif 1903.98<base<=2826.65:
        a=0.075
        de=142.8
        irrf=base*a-de
    elif 2826.65<base<=3751.05:
        a=0.15
        de=354.8
        irrf=base*a-de
    elif 3751.05<base<=4664.68:
        a=0.225
        de=636.13
        irrf=base*a-de
    else:
        a=0.275
        de=869.36
        irrf=base*a-de
    return irrf
print(irrf(base))