import math
v = float (input("Velocidade: "))
ângulo = float(input("Ângulo: "))
d = (((v**2)*(math.sin(math.radians(2*ângulo))/9.8))

if 102 >= d >= 98  :
     print ("Acertou")
elif d < 98:
     print ("Muito perto")
else:
      print("Muito longe") 
   

     

