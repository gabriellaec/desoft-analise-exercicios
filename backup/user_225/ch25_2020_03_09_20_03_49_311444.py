import math
v = float (input("Velocidade: "))
ângulo = float(input("Ângulo: "))
d = (((v**2)*(math.sin(math.radians(2*ângulo))/9.8)

if d > 98 and d < 102 :
     print ("Acertou")
elif d < 98:
     print ("Muito perto")
else:
      print("Muito longe") 
   

     

