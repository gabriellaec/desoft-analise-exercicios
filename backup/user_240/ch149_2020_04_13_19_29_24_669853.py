sb = int(input('qual é o seu salário bruto?'))
ndd = int(input('quantos dependentes você tem?'))

if sb <= 1045:
    inss = sb*0.075
elif sb <= 2089.6:
    inss = sb*0.09
elif sb <= 3134.4:
    inss = sb*0.12
elif sb <= 6101.06:
    inss = sb*0.14
else:
    inss = 671.12

base = sb - inss - ndd*189.59

if base <= 1903.98:
    al = 0
    de = 0
elif base <= 2826.65:
    al = 0.075
    de = 142.8
elif base <= 3751.05:
    al = 0.15
    de = 354.8
elif base <= 4664.68:
    al = 0.225
    de = 636.13
else:
    al = 0.275
    de = 869.36

irrf = base * al - de

print(irrf)



