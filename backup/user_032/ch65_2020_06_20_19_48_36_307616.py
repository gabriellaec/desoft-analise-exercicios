def capitaliza(string):
    palavra = string[::-1]
    for s in palavra:
        x = s.upper()
    word = x + string[1:]
    return word
       