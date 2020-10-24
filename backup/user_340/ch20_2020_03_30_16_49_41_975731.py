a=float(input('qual distancia em km?'))
if a<=200:
    b=0.5*a
else:
    b=0.45*a
print ('R${0:.3f}'.format(b))
    
