def capitaliza(string):
    primeiraletra = string[0:1]
    resto = string[1:]
    primeiraletra = primeiraletra.upper()
    
    string = primeiraletra + resto
    return string