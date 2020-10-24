km=float(input("Qual distância você quer percorrer?"))
if km<=200:
    a= km*0.5
    print{:.2f}.format(a)
else:
    a=100+(km-200)*0.45
    print{:.2f}.format(a)