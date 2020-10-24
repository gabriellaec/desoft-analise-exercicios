deposito=float(input("Qual foi seu deposito inicial?"))
juros=float(input("Qual foi a taxa de juros da poupança?"))
saldo= deposito*juros+deposito
print (saldo)
contador=0
while contador <23:
   saldo=saldo*juros+saldo
   print (saldo)
   contador+=1

b= saldo-deposito

             
             
             
     
             
                