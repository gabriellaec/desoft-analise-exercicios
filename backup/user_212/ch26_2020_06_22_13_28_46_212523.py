valor_casa = float(input(" Qual o valor da casa?"))
salario = float(input("Qual o seu salário"))
anos_a_pagar = int(input("em quantos anos vai pagar ?"))

parcial_salario = salario*0.3
prestacao = valor_casa/(anos_a_pagar*12)

if parcial_salaio > prestacao :
    print ('Empréstimo aprovado')

elif parcial_salario < prestacao :
    print ('Empréstimo não aprovado')