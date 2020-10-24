def remove_vogais(string):
    for x in string:
        if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
            del x
    return string