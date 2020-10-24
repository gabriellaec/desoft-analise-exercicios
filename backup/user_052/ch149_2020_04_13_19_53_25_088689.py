perg = int(input("Qual o salario bruto:" ))
perg2 = int(input("Numero de dependentes:" ))
if perg <= 1045:
    paga = perg * 0.075
if perg > 1045 and perg <= 2089.60:
    paga = perg * 0.09
if perg > 2089.61 and perg <= 3134.40:
    paga = perg * 0.12
if perg > 3134.40 and perg <= 6101.06:
    paga = perg * 0.14
if perg > 6101.06:
    paga = 671.12

if perg <= 1903.98:
    deduçao = 0
    aliquota = 0
if perg > 1903.98 and perg <= 2826.65:
    deduçao = 142.80
    aliquota = 0.075
if perg > 2826.65 and perg <= 3751.05:
    deduçao = 354.80
    aliquota = 0.15
if perg > 3751.05 and perg <= 4664.68:
    deduçao = 636.13
    aliquota = 0.225
if perg > 4664.68:
    deduçao = 869.36
    aliquota = 0.275

base_de_calculo = perg - paga - (perg2 * 189.59)
resultado = (base_de_calculo * aliquota) - deduçao
print (resultado)


 