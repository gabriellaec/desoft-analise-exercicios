a= float(input("Quantos km deseja percorrer?"))
if a <= 200:
    print("Valor da passagem: R${0:.2f}".format(0.50*a))
else:
    print ("Valor da passagem: R${0:.2f}".format(0.50*200+(a-200)*0.45))

