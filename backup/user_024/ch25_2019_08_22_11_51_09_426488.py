km = float(input("Quantos KM?"))

if km<=200:
    preco = km*0.50
else:
    preco =(km-200)*0.45+200*0.5

print ("R${0}" .format(preco))
