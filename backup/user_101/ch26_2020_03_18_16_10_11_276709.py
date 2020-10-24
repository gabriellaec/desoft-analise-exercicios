resp_do_valor=int(input("Qual o valor da casa? "))
resp_do_salario=int(input("Qual o seu salário? "))
resp_do_tempo=int(input("Quantos anos para pagar? ")
prestacao=(resp_do_valor)/(resp_do_tempo*12)
if prestacao>0.3*resp_do_salario:
                  print ("Empréstimo não aprovado")
else:
                  print ("Empréstimo aprovado")
