def remove_vogais(string):
    for i in len(string):
        if string[i] == 'a' or string[i] =='e' or string[i] =='i' or string[i] =='o' or string[i] =='u':
            del string[i]
    return string