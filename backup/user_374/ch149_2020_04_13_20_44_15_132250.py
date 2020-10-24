n_depen = 0
sal_bru = 0

n_depen = int(input('Digite o número de dependentes '))
sal_bru = int(input('Digite o valor do seu salário bruto '))

contri_inss = 0

if sal_bru <= 1045:
    contri_inss = sal_bru * 0.075
elif sal_bru > 1045 and sal_bru <= 2089.60:
    contri_inss = sal_bru * 0.09
elif sal_bru > 2089.60 and sal_bru <= 3134.40:
    contri_inss = sal_bru * 0.12
elif sal_bru > 3134.40 and sal_bru <= 6101.06:
    contri_inss = sal_bru * 0.14
elif sal_bru > 6101.06:
    contri_inss = 671.12

base_cal = sal_bru - contri_inss - (n_depen*(189.59))

aliq = 0
dedu = 0
irrf = 0

if base_cal <= 1903.98:
    aliq = 0
    dedu = 0
    irrf = base_cal * aliq - dedu

elif base_cal > 1903.98 and base_cal <= 2826.65:
    aliq = 0.075
    dedu = 142.8
    irrf = base_cal * aliq - dedu

elif base_cal > 2826.66 and base_cal <= 3751.05:
    aliq = 0.15
    dedu = 354.8
    irrf = base_cal * aliq - dedu

elif base_cal > 3751.05 and base_cal <= 4664.68:
    aliq = 0.225
    dedu = 636.13
    irrf = base_cal * aliq - dedu
    
elif base_cal > 4664.68:
    aliq = 0.275
    dedu = 869.36
    irrf = base_cal * aliq - dedu

print(irrf)
