a=float(input('qual distancia em km?'))
if a<=200:
    b=0.5*a
if a>200:
    b=0.45*a
print ('R${0:.2f}'.format(b))
    
