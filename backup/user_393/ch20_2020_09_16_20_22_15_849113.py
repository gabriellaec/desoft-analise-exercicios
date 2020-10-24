x= int(input("distância percorrida em Km:"))
if x <= 200:
    print("A preço da passagem é {0:.2f}".format(float(x*0.5)))
    
else:
    print("A preço da passagem é {0:.2f}".format(float(100 + 0.45*(x-200))))
