    if d<=200:
        a= d*0.50
    else:
        a= 100+(d-200)*0.45  
d=int(input('distancia?'))
print ('{0:.2f}'.format(a))