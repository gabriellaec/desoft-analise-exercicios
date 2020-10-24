x = float(input('Qual a distancia percorrida?'))
    if x<= 200:
        y = x*0.50
        return y
    elif x>200:
        z = x-200
        return 100 + z*0.45
print(x)
 
