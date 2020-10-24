a=int(input('distancia?'))
if a>200:
    k=(100+(a-200)*0.45)
else:
    k=a*0.50
print('{:.2f}'.format(k))

      
