
    

def eh_crescente(x):
    for i in range(len(x)):
        if x[i-1] < x[i]:
            return True
        else:
            return False
    
    
    
    
    