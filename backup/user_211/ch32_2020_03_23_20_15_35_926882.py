def lista_primos(n):
    if n < 1:
        return[]
    primos = [2]
    x=3
    while len(primos) < n:
        for i in range(2,x):
            if number % i == 0:
            	break 
            if i==number-1:
                primos.append(number)
        number +=1
return primos