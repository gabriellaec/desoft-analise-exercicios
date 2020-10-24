import math

def reflexao_total_interna(n1,n2,theta2):  
    y= math.degrees(math.asin((n1*math.sin(math.radians(theta2)))/n2)) 
    if y>1:
        print("Refração")
    else:
        print("reflexão interna total")
    
   