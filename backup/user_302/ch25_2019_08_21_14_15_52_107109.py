km = int(input("Qual a distância de sua viagem em km? "))
if km <= 200:
  preco = km*0.5
  print("O valor da sua viagem é de R$ {0}".format(preco))
else:
  distancia_extra = km-200
  preco2 = 100+distancia_extra*0.45
  print("O valor da sua viagem é de R$ {0}".format(preco2))