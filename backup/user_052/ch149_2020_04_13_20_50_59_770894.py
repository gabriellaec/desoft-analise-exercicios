perg = float(input("Qual o salario bruto:" ))
if perg <= 1045:
    paga = perg * 0.075
elif perg <= 2089.60:
    paga = perg * 0.09
elif perg <= 3134.40:
    paga = perg * 0.12
elif perg <= 6101.06:
    paga = perg * 0.14
else:
    paga = 671.12

perg2 = int(input("Numero de dependentes:" ))
base_de_calculo = perg - paga - (perg2*189.59)

if base_de_calculo <= 1903.98:
    deduçao = 0
    aliquota = 0
elif base_de_calculo <= 2826.65:
    deduçao = 142.80
    aliquota = 0.075
elif base_de_calculo <= 3751.05:
    deduçao = 354.80
    aliquota = 0.15
elif base_de_calculo <= 4664.68:
    deduçao = 636.13
    aliquota = 0.225
else:
    deduçao = 869.36
    aliquota = 0.275
        
resultado = (base_de_calculo * aliquota) - deduçao
print (resultado)


 