a = float(input('Qual o valor da casa?'))
b = float(input('Qual seu salário?'))
c = int(input('Em quantos anos a casa será paga?'))

if a/(12*c) < 0.3*b:
   print ('Empréstimo aprovado')
else:
   print ('Empréstimo não aprovado')
        