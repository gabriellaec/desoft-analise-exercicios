d=float(input("distancia em km"))
if d<=200:
    a=0.5*d
else:
    a=100+(d-200)*0.45
        
print('{:.2f}'.format(a))