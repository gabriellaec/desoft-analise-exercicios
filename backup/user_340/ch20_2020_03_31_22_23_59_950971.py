a=float(input('qual distancia em km?'))
if a<=200:
    b=0.5*a
if a>200:
    b=0.5*200 + 0.45*(a-200)
print("{0:.2f}".format(b))
    
