fibonacci=[0]*n
fibonacci[0]=1
fibonacci[1]=1
i=0
while(i<n-2):
    calcula_fibonacci[i+2]=fibonacci[i+1]+fibonacci[i]
    i=i+1
    
print(calcula_fibonacci)

