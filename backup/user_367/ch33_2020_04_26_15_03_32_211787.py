def primos_entre(a, b):
    divisions = 0
    response = False
    number = int(number)
    if number:
        for i in range(1, number + 1):
            if number % i == 0:
                divisions = divisions + 1
            if divisions == 2:
                response = True
    if divisions > 2:
        response = not response
    return response
 
