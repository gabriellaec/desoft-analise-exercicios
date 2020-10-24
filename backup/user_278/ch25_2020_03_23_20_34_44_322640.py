import math
v = float(input("v= ")
a = float(input("a= ")

d=(v**2)*math.sin(radians(2*a))/(9.8)
         if d <98:
         	print ("Muito perto")
         elif d<=102 or d>=98:
         	print ("Acertou!")
         else:
            print ("Muito longe")