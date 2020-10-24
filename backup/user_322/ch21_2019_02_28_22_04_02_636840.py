a = int(input("Quantos Km vc vai viajar?"))

if a <= 200:
    preco = a * 0.5
    
else: 
    preco = a * 0.5 + (a - 200) * 0.45
    
print("{0:.2f}".format(preco))