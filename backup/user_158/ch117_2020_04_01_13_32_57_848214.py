import math
def snell_descartes(n1,n2,teta1):
   x = math.sin(math.radians(teta1))*n1/n2
   y = math.asin(x)
   teta2=math.degrees(y)
   return teta2