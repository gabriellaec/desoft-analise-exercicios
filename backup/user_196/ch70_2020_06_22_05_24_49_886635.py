def esconde_senha(string):
    for i in range (len(string)):
        nova = string.replace(string[i],'*')
        return nova
