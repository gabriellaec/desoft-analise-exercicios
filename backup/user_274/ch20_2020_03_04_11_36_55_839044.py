dist = float(input("Qual a distância que você quer percorrer? (km) "))
extra = dist-200

if extra > 0:
    preco = 200*.5 + extra*.45
else:
    preco = dist*.50
    
print("R${0: .2f}".format(preco))