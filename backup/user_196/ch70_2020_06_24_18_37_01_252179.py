def esconde_senha(string):
    nova = ''
    for i in string:
        nova = string.replace(string[i],'*')
    return nova
