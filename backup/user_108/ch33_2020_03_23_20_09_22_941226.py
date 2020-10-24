
def primos_entre(a,b):
    n = b - a
    if n < 1:
        return []
    primos = [2]
    number = a
    while len(primos) < n:
        for i in range(2,number):            
            if number % i == 0:
                break 
            if i == number-1:
                primos.append(number)
        number += 1
    return primos

