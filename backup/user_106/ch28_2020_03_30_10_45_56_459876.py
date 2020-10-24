e=[0]*100
x=0
i=0

while x<100:
    e[i]=1/(2**x)
    x+=1
    i+=1
    
print(sum(e))