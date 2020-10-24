salario = int(input("Qual o valor do salario?"))
dependentes = int(input("Qual o numero de dependentes?"))
aliquota = 0
if salario <= 1045:
    aliquota = 0.075*salario
else: 
    aliquota = 0.09*salario
    if salario <= 3134.4:
        aliquota = 0.12*salario
        if salario <= 6101.06:
            aliquota = 0.14*salario
            if salario > 6101.06:
                aliquota = 671.12