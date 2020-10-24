x = int(input('distancia'))
if x <= 200:
    return x*0.5
elif x > 200:
    return 200*0.5 + (x-200)*0.45
print(x)