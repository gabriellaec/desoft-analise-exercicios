
salario = float(input("Digite seu salário bruto: "))
num_dep = float(input("Digite o numero de dependentes: "))
inss = 0

#calcula contribuição para o INSS
if salario < 1045.01:
    inss = salario*0.075
    
elif 1045.01 <= salario < 2089.61:
    inss = salario*0.09
    
elif 2089.61 <= salario < 3134.41:	
    inss = salario*0.12
    
elif 3134.41 <= salario < 6101.07:
    inss = salario*0.14
    
else:
    inss = 671.12
    
#Base de cálculo 
bdc = salario - inss - (num_dep*189.59)
deducao = 0

if bdc < 1903.99:
    bdc = bdc
    deducao = 0
    
elif 1903.99 <= bdc < 2826.66:
    bdc = bdc*0.075
    deducao = 142.80
    
elif 2826.66 <= bdc < 3751.06:
    bdc = bdc*0.15
    deducao = 354.80
    
elif 3751.06 <= bdc < 4664.69:
    bdc = bdc*0.225
    deducao = 636.13
    
else:     
    bdc = bdc*0.275
    deducao = 869.36

#print IRFF
print(bdc-deducao)
  