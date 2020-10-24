d=float(input("qual é a distância"))
if d <= 200:
    print('{0:.2f}'.format(d*0.5))
elif d>200:
    x = d - 200
    c= d - x
    a= x*0.45
    z= c*0.5
    f= c + a
    print('{0:.2f}'.format(f))
   