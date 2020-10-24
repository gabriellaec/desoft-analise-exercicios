import math 
def snell_descartes(n1,n2,o1):
   math.sin(math.radians(o2))  =  o2
   o2 =n1 * math.sin(math.radians(o1)) / n2
   return o2

n1 = 1/2
n2 = 1
o1 = 90
sd = snell_descartes(n1,n2,o1)
print(sd)