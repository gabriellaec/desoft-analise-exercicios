def esconde_senha (string):
    i = 0
    while i < len(string):
        a = string.replace(string[i],"*")
        palavra += a
        i += 1
    return palavra

    