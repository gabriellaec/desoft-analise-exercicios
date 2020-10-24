def is_odd (number):
    return number % 2 = 1

def soma_impares (numbers):
    result = 0
    
    for number in numbers:
        if is_odd(number):
            result += number
            
    return result
