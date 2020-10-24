calcula_fibonacci=[0]*n
calcula_fibonacci[0]=1
calcula_fibonacci[1]=1
i=0
while(i<n-2):
    calcula_fibonacci[i+2]=calcula_fibonacci[i+1]+calcula_fibonacci[i]
    i=i+1
    
print(calcula_fibonacci)

