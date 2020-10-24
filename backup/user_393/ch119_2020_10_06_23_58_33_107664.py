import math
#def calcula_euler(x,n):
 #   i=0
  #  soma=0
   # while i<n:
    #    y=(x**i)/math.factorial(i)
     #   i+=1
      #  soma+=y
   # return soma

    
import math
def calcula_euler(x,n):
    soma= 0
    i= 0
    while i < n:
        soma= soma + (x**i)/math.factorial(i)
        i= i + 1
    return soma
        