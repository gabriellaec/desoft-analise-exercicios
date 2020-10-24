def remove_vogais(string):
    i = 0
    while i < len(string):
        word = string[i]
        if word == 'a':
            string = string.replace(word, '')
        elif word == 'e':
            string = string.replace(word, '')
        elif word == 'i':
            string = string.replace(word, '')
        elif word == 'o':
            string = string.replace(word, '')
        elif word =='u':
            string = string.replace(word, '')
        i += 1
    return string