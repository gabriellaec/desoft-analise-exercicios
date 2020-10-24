a= float(input("distancia que vai percorrer em km :"))
if a <= 200:
    y=0.50*a
else:
    y=(a-200)*0.45 + 100
    
print ("{0:.2f}".format(y))
    
