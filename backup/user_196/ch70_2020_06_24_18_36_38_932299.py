def esconde_senha(string):
    for i in string:
        nova = string.replace(string[i],'*')
    return nova
