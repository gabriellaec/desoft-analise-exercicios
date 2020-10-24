i=0
while(i<100):
    x=1/(2**i)
    i+=1
    x+=1/(2**(i+1))
print(x)