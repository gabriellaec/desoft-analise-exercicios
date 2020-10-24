km=int(input("distância a percorrer")) 
if km <= 200:
   print (km*0.5)
else:
    print (200*0.5 + ((km-200)*0.45)