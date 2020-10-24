
    

def eh_crescente(x):
    a = 1
    for a in range(len(x)):
        if x[a-1] < x[a]:
            return True
        else:
            return False
    
    
    
    
    