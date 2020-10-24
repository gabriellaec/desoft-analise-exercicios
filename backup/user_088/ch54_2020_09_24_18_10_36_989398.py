def  calcula_fibonacci(fibonacci):
    i=0
    fibonacci=[0]*n
    fibonacci[0]=1
    fibonacci[1]=2
while(i<n):
      fibonacci[i+2]=fibonacci[i+1]+fibonacci[i]
      i+=1
        return (fibonacci)