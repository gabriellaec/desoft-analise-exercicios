x = float(input('distancia'))
if x <= 200:
    print(x*0.5)
elif x > 200:
    print(200*0.5 + (x-200)*0.45)