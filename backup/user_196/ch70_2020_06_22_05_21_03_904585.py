def esconde_senha(string):
    for i in string:
        return string.replace(string[i],'*')
