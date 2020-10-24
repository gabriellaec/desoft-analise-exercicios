a=float(input('distância percorrida'))
if a<=200:
    c=a*0.5
else:
    b=a-200
    c=100+b*0.45
print({0:.2f}.format(c))
    