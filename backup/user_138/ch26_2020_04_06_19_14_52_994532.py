valor=input("Qual o valor da casa?")
salario=input("Qual o valor do seu salário?")
anos=input("Em quantos anos planeja pagar?")
meses=anos*12
prestacaomensal=valor/meses
maximo=salario*0,3
if prestacaomensal<maximo:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')