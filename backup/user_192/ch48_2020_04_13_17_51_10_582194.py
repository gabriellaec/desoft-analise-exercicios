
    

def eh_crescente(x):
    a = 1
    for a in range(len(x)):
        if x[a-1] < x[a]:
            a+=1
            return True
        else:
            return False
    
    
    
    
    