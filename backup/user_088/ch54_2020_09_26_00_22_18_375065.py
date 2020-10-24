def  calcula_fibonacci(n):
    i=2
    fibonacci=[]
    fibonacci[0]=1
    fibonacci[1]=1
    while(i<n):
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
        i+=1
    return (fibonacci)