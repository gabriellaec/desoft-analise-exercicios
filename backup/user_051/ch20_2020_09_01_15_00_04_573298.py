d=int(input('distancia em km: '))
if d <= 200:
    p=d*0.5
    print ("%.2f"%p)
if d > 200:
    p=200*0.5 + (d-200)*0.45
    print ("%.2f"%p)