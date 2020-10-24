velocidade = input(int("Qual era a velocidade do carro em km/h?:")
if velocidade > 80:
   multa = round((velocidade-80)*5,2)
   print("Sua multa é de R${0}".format(multa))
else:
   print("Não foi multado")