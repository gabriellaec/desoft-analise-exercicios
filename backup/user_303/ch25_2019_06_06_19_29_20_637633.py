a=float(input("Qual a distância da viagem?"))

if a<=200:
    x=0.5*a
else:
    x=0.5*200+(a-200)*0.45
    
print("{0:.2f}".format(x))