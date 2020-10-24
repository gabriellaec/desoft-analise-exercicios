def esconde_senha (string):
    b = len(string)
    i = 0
    while i < b:   
        a = string.replace(string[i],"*")
        i += 1
        return a
    