t=0  
i=0
maximo=0

while(i<1000):
    num=i
    c=1
    
    if(i!=0):
        while(num!=1):
        
            if(num%2==0):
                num=num/2
            else:
                num=3*num+1 
        
            c+=1 
    
    if(c>t):
        t=c
        maximo=i
    i+=1  

print(maximo)