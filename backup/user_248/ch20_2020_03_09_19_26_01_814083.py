km=float(input("Qual distância você quer percorrer?"))
if km<=200:
    print(km*0.5)
else:
    print(100+(km-200)*0.45)