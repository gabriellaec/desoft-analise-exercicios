def capitaliza(string):

    upper_string = ''

    a_0 = string[:1]
    a = a_0.upper()
    upper_string += a

    for caracter in string[1:]:
        upper_string += caracter

    return upper_string