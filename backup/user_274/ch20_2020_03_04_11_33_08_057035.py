dist = float(input("Qual a distância que você quer percorrer? (km) "))

if dist <= 200:
    preco = dist*.5
else:
    preco = dist*.45
    
print("R${0: .2f}".format(preco))