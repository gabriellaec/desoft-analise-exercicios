def  calcula_fibonacci (n):
    
    fibonacci = [0]*100
    fibonacci[1] = 1
    fibonacci[0] = 1
    n=2
while(n<100):
    fibonacci[n] = fibonacci[n-1]+fibonacci[n-2]
    n = n + 1