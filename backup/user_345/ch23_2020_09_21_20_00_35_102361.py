velocidade = int(input('Qual a velocidade do seu carro? '))
if velocidade > 80 :
   m = (velocidade - 80) * 5.0
   print ('Você foi multado com uma multa de {0} reais'. format (m))
else:
   print ('Não foi multado')