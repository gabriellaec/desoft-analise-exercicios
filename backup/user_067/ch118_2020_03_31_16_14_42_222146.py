import math
def reflexao_total_interna(n1,n2,theta_1):
    sin_theta_2 = n1*math.sin(math.rad(theta_1))/n2
    
    theta_2 = math.degrees(math.asin(sin_theta_2))
    if(theta_2>90):
        return False
    else:
        return True
