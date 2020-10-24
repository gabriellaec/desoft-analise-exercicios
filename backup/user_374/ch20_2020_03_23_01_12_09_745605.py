d = (input("Distância em km"))
x = int(d)
    
if x <= 200:
        calculo = x*0.5
        print('{0:.2f}'.format(calculo))
else:
        calcula = (200*0.5 + (x-200)*0.45)
        print('{0:.2f}'.format(calcula))
