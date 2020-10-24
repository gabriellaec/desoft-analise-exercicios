distancia = int(input("qual a distancia?"))
if d<= 200:
    valor = d*0.5
else:
    valor = (d-200)*0.45 + 200*0.5
print("valor {0:.2f}".format(valor))       
    