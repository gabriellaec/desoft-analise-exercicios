salario_b = float(input("Informe o seu salário bruto aqui: "))
n_dependentes = int(input("Informe o número de dependentes do usuário: "))
while salario_b>0.00:
    if salario_b>0 and salario_b<1045:
        inss= salario_b*0.075
    elif salario_b>1045.01 and salario_b<2089.0:
        inss= salario_b*0.09
    elif salario_b>2089.01 and salario_b<3134.40:
        inss=salario_b*0.12
    elif salario_b>3134.41 and salario_b<6101.06:
        inss=salario_b*0.14
    elif salario_b>6101.06:
        inss=671.12
        
base_calculo = salario_b - inss- (n_dependentes*189.59)


while base_calculo>0:
    if base_calculo<1903.98:
        aliquota=0.0
        deducao=0.0
    elif base_calculo>1903.99 and base_calculo<2826.65:
        aliquota=0.75
        dedução=142.80
    elif base_calculo>2826.66 and base_calculo<3751.05:
        aliquota=1.5
        deducao=354.80
    elif base_calculo>3751.06 and base_calculo<4664.68:
        aliquota=2.25
        deducao=636.13
    elif base_calculo>4664.68:
        aliquota=2.75
        deducao=896.36

irrf=base_calculo*aliquota-deducao
print(irrf)

        
    