valor=input("Qual o valor da casa?")
salario=input("Qual o valor do seu salário?")
tempo=input("Em quantos anos planeja pagar?")*12
prestacaomensal=valor/tempo
maximo=salario*0,3
if prestacaomensal<maximo:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')