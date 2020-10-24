import math
def reflexao_total_interna(n1,n2,theta_1):
    sin_theta_2 = n2*math.sin(math.radians(theta_1))/n1
    
    theta_2 = math.degrees(math.asin(sin_theta_2))
    if(theta_2>90):
        return False
    else:
        return True
