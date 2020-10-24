def esconde_senha(string):
    for i in range (len(string)):
        return string.replace(string[i],'*')
