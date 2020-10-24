valor = int(input('quantos cigarros voce fuma por dia?' ))
salario = int(input('a quantos anos fuma?' ))
anos = int(input('anos?' )
prestação = valor/(anos*12)  
if prestação > salario*30/100:
           print('Empréstimo não aprovado')
else:
           print('Empréstimo aprovado')
