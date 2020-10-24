a = float(input("Qual distância tu desejas percorrer? "))

if a <= 200:
    p1 = a*0.50
    print("{0:.2f}".format(p1))
else:
    p2 = 100 + (a - 200)*0.45
    print("{0:.2f}".format(p2))
    
    
    