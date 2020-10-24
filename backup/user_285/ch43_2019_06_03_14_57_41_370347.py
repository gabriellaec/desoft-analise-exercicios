n=0
contador=0
while n<1000:
    if n%2==0:
        N= n/2
        contador+=1
    else:
        N=3*n+1
        contador+=1
    n+=1