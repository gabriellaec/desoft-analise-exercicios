a = float(input("Qual o seu salário bruto?: "))
b = float(input("Qual o número de dependentes do usuário?: "))

if a <= 1045:
    contribuicao = a * 0.075
    print("Essa {0} é a sua contribuição para o INSS!". format(contribuicao))

elif 1045.01 <= a<= 2089.60:
    contruibuicao = a * 0.09
    print("Essa {0} é a sua contribuição para o INSS!". format(contribuicao))
    
elif 2089.61 <= a <= 3134.40:
    contribuicao = a * 0,12
    print("Essa {0} é a sua contribuição para o INSS!". format(contribuicao))

elif 3134.41 <= a <= 6101.06:
    contribuicao = a * 0,14
    print("Essa {0} é a sua contribuição para o INSS!". format(contribuicao))

elif a>= 6101.67:
    contribuicao = 671.12

base_de_calculo = a - contribuicao - (b*189.59)
if base_de_calculo <= 1903.98:
    aliquota = 0
    deducao = 0
elif 1903.99 <= base_de_calculo <= 2826.65:
    aliquota = 0.075
    deducao = 142.80
elif 2826.66 <= base_de_calculo <= 3751.05:
    aliquota = 0.15
    deducao = 354.80
elif 3751.06 <= base_de_calculo <= 4664.68:
    aliquota = 0.225
    deducao = 636.13
elif base_de_calculo >= 4664.68:
    aliquota = 0.275
    deducao = 869.36
irff = base_de_calculo * (aliquota - deducao)
print (irff)
