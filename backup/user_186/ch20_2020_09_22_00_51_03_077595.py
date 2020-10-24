#Preço da Passagem
km=float(input("Quantos km? "))
taxa=5/10
Preco=taxa*km
if km<=200:
    Preco=taxa*km
else:
    Preco=taxa*km+(45/100)*km
print ("A passagem custa: ", Preco)