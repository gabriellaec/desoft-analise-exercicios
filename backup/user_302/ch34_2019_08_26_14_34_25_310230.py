deposito = float(input("Qual valor do seu deposito? "))
taxa =  float(input("Qual a taxa de juros em porcentagem ao mês? "))
mes = 1
while mes <= 24:
  ganho = deposito*taxa**mes
  print("Mês {0} : R$ {1}".format(mes, ganho))
  mes = mes+1
juros_total = (deposito*taxa**24)-deposito
print ("Você lucrou {0}".format(juros_total))