km=int(input("Distancia: "))
if km<=200:
    p=0.5*200
    print("{0:.2f}".format(km))
else:
    p=0.5*200+0.45*(km-200)
    print("{0:.2f}".format(km))
    

    
