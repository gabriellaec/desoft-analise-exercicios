from math import sin, radians
v= float(input("v= "))
ao= float(input("ao= "))

d=(v**2)*.sin(radians(2*ao))/(9.8)
if d <98:
    print ("Muito perto")
elif d<=102 or d>=98:
    print ("Acertou!")
else:
    print ("Muito longe")