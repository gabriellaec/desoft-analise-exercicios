def capitaliza(string):
    letra = string[0]
    resto = string[1:]
    return f'{letra.upper()}{resto.lower()}'