
a=int(input('qual a distancia?'))
if a>200:
    b=100+(a-200)*0.45
else:
    b=a*0.5
print("{0:.2f}".format(b))