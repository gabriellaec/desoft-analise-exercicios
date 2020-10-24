sal = int(input("Qual o valor do seu salário bruto? "))
dep = int(input("Quandos dependentes você tem? "))

if sal <= 1045:
    contri = sal*.075
elif sal <= 2089.6:
    contri = sal*0.09
elif sal <= 3134.4:
    contri = sal*.12
elif sal <=6101.06:
    contri = sal*.14
else:
    contri = 671.12

base = sal - contri - dep*189.59

if sal <= 1909.98:
    ali = 0
    ded = 0
elif sal <= 2826.65:
    ali = .075
    ded = 142.8
elif sal <= 3751.05:
    ali = .15
    ded = 354.8
elif sal <= 4664.68:
    ali = .225
    ded = 636.13
else:
    ali = .275
    ded = 869.36

irrf = base*ali-ded

print(irrf)