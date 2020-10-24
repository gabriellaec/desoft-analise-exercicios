def lista_primos(numero):
    if numero<1:
        return []
    primo = [2]
    number = 1
    while len(primo)<numero:
        for i in range (2,number):
            if number % i ==0:
                break
            if i == number-1:
                primo.append(number)
        number +=1
    return primo
        
       