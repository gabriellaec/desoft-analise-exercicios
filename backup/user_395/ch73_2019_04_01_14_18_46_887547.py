def remove_vogais(string):
    for elemento in string:
        if elemento == 'a' or elemento == 'e' or elemento == 'i' or elemento == 'o' or elemento == 'u':
            del elemento
        return string
print (remove_vogais('dora'))