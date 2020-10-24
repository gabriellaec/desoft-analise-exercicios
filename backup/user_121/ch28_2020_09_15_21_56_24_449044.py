i=0
x=1/(2**i)
while(i<100):
    i+=1
    x+=1/(2**(i+1))
print(x)