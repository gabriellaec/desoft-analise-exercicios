d = float(input("Quantos km:"))

if d <200:
    p = 0.50*d
else:
    p = 0.50*d + 0.45*(d-200)
    
print(round(p,2))