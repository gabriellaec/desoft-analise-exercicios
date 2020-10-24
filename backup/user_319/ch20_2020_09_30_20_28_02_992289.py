x = int(input('distancia'))
if x <= 200:
    print({0:.2f}.format(float(x*0.5)))
else x > 200:
    print({0:.2f}.format(float(200*0.5 + (x-200)*0.45)))