salariobruto = float(input("O seu sálario bruto é:"))
numerodedependentes = int(input("O seu número de dependentes é:"))

#Contribuição do INSS#

if salariobruto <= 1045:
    aliquota = 0.075
    contribuicao = salariobruto*aliquota
elif salariobruto <= 2089.6:
    aliquota = 0.09
    contribuicao = salariobruto*aliquota
elif salariobruto <= 3134.4:
    aliquota = 0.12
    contribuicao = salariobruto*aliquota
elif salariobruto <= 6101.6:
    aliquota = 0.14
    contribuicao = salariobruto*aliquota
else:
    contribuicao = 671.12
base = salariobruto - contribuicao - numerodedependentes * 189.59

if base <= 1903.98:
    aliquota = 0.0
    deducao = 0.0
elif base <= 2826.65:
    aliquota = 0.075
    deducao = 142.80
elif base <= 3751.05:
    aliquota = 0.15
    deducao = 354.80
elif base<= 4664.68:
    aliquota = 0.225
    deducao = 869.36
else:
    aliquota = 0.275
    deducao =869.36

irrf = base * aliquota - deducao
print(irrf)