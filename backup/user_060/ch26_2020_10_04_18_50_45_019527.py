casa = int(input("qual o valor da casa: "))
salario = int(input("qual o seu salario: "))
prazo = int(input("quantos anos para pagar: "))

prestacao = (casa / prazo*12)
            
if prestacao > salario*0.3:
    print('Empréstimo não aprovado')
else:
     print('Empréstimo aprovado')       