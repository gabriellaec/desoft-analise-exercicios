vel= float(input("velocidade:"))
if vel>80:
        y= 5*(vel-80)
        print ("{0:.2f}".format(y))
else:
    print ("Não foi multado")