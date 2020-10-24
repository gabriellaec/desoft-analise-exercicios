depósito=float(input("Depósito incial: "))
taxa=float(input("Taxa: "))
mes=1

while mes<=24:
   saldo=saldo+(saldo*(taxa))
   print("Saldo do mes{0} é de {saldo:.2f}".format(mes)
   mes +=1
print ("O ganho obtido com os juros foi de {0:.2f}".format(saldo)