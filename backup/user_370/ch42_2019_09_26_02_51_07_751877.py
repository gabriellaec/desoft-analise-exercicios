def quantos_uns(x):
    z=0
    while x > 0:
        if x%10==1:
            z+=1 
        x=x//10
    return (z)
    
a= quantos_uns(10)
print (a)