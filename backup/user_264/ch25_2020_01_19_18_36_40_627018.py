d = float(input("Quantos km:"))

if d <200:
    p = 0.50*d
else:
    p = 101 + 0.45*(d-200)
    
print(round(p,2))