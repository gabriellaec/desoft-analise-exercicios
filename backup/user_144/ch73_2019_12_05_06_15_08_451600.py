def remove_vogais(string):
    new_string = ''
    for vogal in string:
        if vogal not in 'aeiou':
            new_string += vogal
    return new_string