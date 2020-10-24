d=float(input("qual é a distância"))
if d <= 200:
    print('{0:.2f}'.format(d*0.5))
elif d>200:
    x=(d-200)*0.45 + 200 * 0.5  
    print('{0:.2f}'.format(x))
   