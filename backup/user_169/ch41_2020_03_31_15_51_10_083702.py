num=[-3,-2,-1,0,1]

def zera_negativos(num):
    
    i=0
    
    while i<len(num):
        if num[i]<0:
            num[i]=0
        i+=1        
    
    return num

       