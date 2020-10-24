salario = int(input("Qual o valor do salario?"))
dependentes = int(input("Qual o numero de dependentes?"))
INSS = 0
if salario <= 1045:
    INSS = 0.075*salario
else: 
    INSS = 0.09*salario
    if salario <= 3134.4:
        INSS = 0.12*salario
        if salario <= 6101.06:
            INSS = 0.14*salario
            if salario > 6101.06:
                INSS = 671.12
base = salario - INSS - dependentes*189.59
if base <= 1903.98:
    aliquota = 0
    deducao = 0
else:
    aliquota = 0.075
    deducao = 142.8
    if base <= 3751.05:
        aliquota = 0.15
        deducao = 354.80
        if base <= 4664.68:
            aliquota = 0.225
            deducao = 636.13
            if base > 4664.68
            aliquota = 0.275
            deducao = 869.36
              
irrf = base*aliquota