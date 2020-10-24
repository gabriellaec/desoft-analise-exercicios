d=float(input("qual é a distância"))
if d <= 200:
    print('{0:.2f}'.format(d*0.5))
elif d>200:
    x = d - 200
    a= x*0.45
    while d <= 200:
        b = d*0.5
    c = a + b
    print('{0:.2f}'.format(c))
  