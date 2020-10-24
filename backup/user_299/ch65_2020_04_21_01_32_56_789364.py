def capitaliza(string):
    primeiraletra = string[0:1]
    resto = string[1:]
    primeiraletra = primeiraletra.upper()
    resto = resto.lower()
    string = primeiraletra + resto
    return string