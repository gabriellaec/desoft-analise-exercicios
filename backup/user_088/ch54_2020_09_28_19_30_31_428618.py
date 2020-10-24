def  calcula_fibonacci(n):
    i=2
    fibonacci=[1,1]
    if(n==1):
        return [fibonacci[0]]
    while(i<n):
        lista1=fibonacci[i-1]+fibonacci[i-2]
        fibonacci+=[lista1]
        i+=1
    return (fibonacci)