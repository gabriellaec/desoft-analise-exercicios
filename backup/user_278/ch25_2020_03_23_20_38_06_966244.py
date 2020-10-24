from math import sin, radians
v= float(input("v= "))
a= float(input("ao= "))

d=(v**2)*sin(radians(2*a))/(9.8)
if d <98:
    print ("Muito perto")
elif d <=102 and d >=98:
    print ("Acertou!")
else:
    print ("Muito longe")