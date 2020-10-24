def lista_primos(n):
    if n < 1:
        return []
    primos = [2]
    number = 1
    while len(primos) < n:
        for i in range(2,number):            
            if number % i == 0:
                break 
            if i == number-1:
                primos.append(number)
        number ++
    return primos
