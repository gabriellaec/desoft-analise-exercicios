km = int(input("Quantos KM?"))

if km<=200:
    preco = km*0.50
else:
    preco =(km-200)*0.45+100

print ("R${0:.02f}" .format(preco))
