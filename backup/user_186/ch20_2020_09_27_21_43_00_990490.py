#Preço da Passagem
km=float(input("Quantos km? "))
taxa=5/10
Preco=taxa*km
if km<=200:
    Preco=taxa*km
else:
    Preco=200*(5/10)+(45/100)*(km-200)
print ("A passagem custa: {:.2f}".format(Preco))