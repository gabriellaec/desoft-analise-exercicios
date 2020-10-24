distancia=float(input("Quanto deseja percorrer?"))

if(distancia>200):
    res=0.50*200+(distancia-200)*0.45
    print("{:.2f}".format(res))
else:
    res=0.50*distancia
    print("{:.2f}".format(res))
    
    
    
    