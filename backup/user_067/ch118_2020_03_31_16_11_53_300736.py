import math
def reflexao_total_interna(n1,n2,theta1):
    sin_theta_2 = n1*math.sin(theta_1)/n2
    theta_2 = math.asin(sin_theta_2)
    if(theta_2>90):
        return True
    else:
        return False
