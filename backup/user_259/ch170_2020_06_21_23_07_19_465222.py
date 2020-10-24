def apaga_repetidos(string):
    new_str = str()
    for letter in string:
        if letter not in new_str:
            new_str += letter
        else:
            new_str += '*'
    return new_str