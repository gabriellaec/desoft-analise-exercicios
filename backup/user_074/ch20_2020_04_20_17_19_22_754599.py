d= int(input("distancia em km:"))
if d<200 or d==200:
    p=d*0.50
    print(p)
else:
    p=100+(d-200)*0.45
    print (p)
  