deposito=float(input("Depósito incial: "))
taxa=float(input("Taxa: "))
mes=1

while mes<=24:
   deposito=deposito+(deposito*(taxa))
   print("Saldo do mes{0} é de {1:.2f}".format(mes,deposito)
   mes+=1
print ("O ganho obtido com os juros foi de {0:.2f}".format(deposito)