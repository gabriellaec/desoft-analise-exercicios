a=int(input("A distância que irá percorrer em km"))
if a<=200:
    b = 0.5*a
else:
    b = 100+(a-200)*0.45
    
print('{0:.2f}'.format(b))