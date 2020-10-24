
def primos_entre(a,b):
    primos = []
    if a < 2:
        primos.append(2)
    for number in range(a,b):
        for i in range(2,number):            
            if number % i == 0:
                break 
            if i == number-1:
                primos.append(number)
        number += 1
    return primos

