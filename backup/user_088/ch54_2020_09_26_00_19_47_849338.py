def  calcula_fibonacci(n):
    i=0
    fibonacci=[]
    fibonacci[0]=1
    fibonacci[1]=1
    while(i<n):
        fibonacci[i+2]=fibonacci[i+1]+fibonacci[i]
        i+=1
    return (fibonacci)