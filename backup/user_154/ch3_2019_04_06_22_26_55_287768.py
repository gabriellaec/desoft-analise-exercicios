if sigma == 0:
        return -1
    
    if (x == 0 or mi == 0) and (sigma == x or sigma == mi) and sigma == 1/math.sqrt(2*math.pi):
        return math.exp(-0.5)
    
    parte1 = 0.0
    parte2 = 0.0
    
    if sigma == 1.0:
        parte1 = math.sqrt(2*math.pi)
    elif sigma == 1/math.sqrt(2*math.pi):
        parte1 = 1.0
    elif sigma < 1:
        return 0
    else:
        parte1 = sigma*math.sqrt(2*math.pi)
    
    if x == mi or (x == 0 and y == 0):
        parte2 = 1.0
    elif x == -mi:
        parte2 = math.exp(-0.5(2*x/sigma)**2)
    elif (x == 0 or mi == 0) and (sigma == x or sigma == mi):
        parte2 = math.exp(-0.5)
    else:
        parte2 = math.exp(-0.5((x - mi)/sigma)**2)
    
    return parte2/parte1