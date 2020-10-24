x = int(input('distancia'))
if x <= 200:
    print({0:.2f}.format(x*0.5))
elif x > 200:
    print({0:.2f}.format(200*0.5 + (x-200)*0.45))