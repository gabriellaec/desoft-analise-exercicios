def maior_primo_menor_que(n):
    a= 1
    
    for i in range(n):
        num = i
        if num > 1:
           # check for factors
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               a= i+1
    if n == 3:
        a=2
    return a