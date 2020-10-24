def remove_vogais(string):
    if string=='aeiou':
        return ''
    else:
        for x in string:
            if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
                del x
                return string
        

    