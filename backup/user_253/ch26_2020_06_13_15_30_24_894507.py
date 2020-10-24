valor = int(input('quantos cigarros voce fuma por dia?' ))
salario = int(input('a quantos anos fuma?' ))
anos = int(input('anos?' ))
meses = anos * 12
prestacao = valor / meses  
if prestacao > salario*30/100:
           print('Empréstimo não aprovado')
else:
           print('Empréstimo aprovado')
