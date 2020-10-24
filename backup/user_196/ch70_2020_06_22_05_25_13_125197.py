def esconde_senha(string):
    nova = 0
    for i in range (len(string)):
        nova = string.replace(string[i],'*')
    return nova
