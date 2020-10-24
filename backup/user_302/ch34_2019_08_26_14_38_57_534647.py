deposito = float(input("Qual valor do seu deposito? "))
taxa =  float(input("Qual a taxa de juros em porcentagem ao mês? "))
mes = 1
while mes <= 24:
  ganho = deposito*(1+(taxa/100))**mes
  print("Mês {0} : R$ {1:.2f}".format(mes, ganho))
  mes = mes+1
juros_total = (deposito*(1+(taxa/100))**24)-deposito
print ("Você lucrou {0:.2f}".format(juros_total))