depósito=float(input("Depósito incial: ")
taxa=float(input("Taxa: "))
mes=1

while mes<=24:
   saldo=saldo+(saldo*(taxa/100))
   print("Saldo do mes{0} é de {1:.2f}".format{mes},{saldo})
   mes +=1
print ("O ganho obtido com os juros foi de {0:.2f}".format{saldo})
