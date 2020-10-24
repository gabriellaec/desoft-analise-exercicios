distancia = int(input("qual a distancia?"))
if d<= 200:
    valor = d*0.5
    return valor
else:
    valor = (d-200)*0.45 + 200*0.5
    return valor 
print("valor {0:.2f}".format(float(valor)))        
    