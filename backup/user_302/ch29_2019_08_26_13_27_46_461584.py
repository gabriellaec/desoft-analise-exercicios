def calcula_aumento(a):
  y = 1250-a
  return y
salario = int(input("Qual seu salário?"))
if calcula_aumento(salario) >= 0:
  aumento = salario*1.15
  print ("Seu salário com aumento é {0}".format(aumento))
else:
  aumento2 = salario*1.1
  print("Seu salário com aumento é {0}".format(aumento2))