km=float(input("Qual distância você quer percorrer?"))
if km<=200:
    print({:.2f}.format(km*0.5))
else:
    print({:.2f}.format(100+(km-200)*0.45))