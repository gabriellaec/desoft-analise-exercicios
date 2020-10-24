fibonacci=[0]*n
fibonacci[0]=1
fibonacci[1]=1
i=0
while(i<n):
    calcula_fibonacci[i]=fibonacci[i-1]+fibonacci[i-2]
    i=i+1
    
print(calcula_fibonacci)

