a= float(input("distancia que vai percorrer em km :"))
if a <= 200:
    y=0.50*a
else:
    y=0.45*a-(a*200)
    
print (y)
    
