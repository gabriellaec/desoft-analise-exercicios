def primos_entre(a,b):
    primo = 0
    for num in range(lower,upper + 1):  
        if num > 1:  
            for i in range(2,num):  
                if (num % i) == 0:  
                    break  
            else:  
                primo += 1 
    return primo