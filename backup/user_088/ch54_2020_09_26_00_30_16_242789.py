def  calcula_fibonacci(n):
    i=2
    fibonacci=[1,1]
    if(n==1):
        return fibonacci[0]
    while(i<n):
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
        i+=1
    return (fibonacci)